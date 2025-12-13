# In the house purchase model, the key "risk" of cash is the duration mismatch.

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def simulate_hull_white(
	n_years = 3,
	n_scenarios = 2000,
	dt = 1/12,

	# 1. Hull-White Parameters
	a = 0.3,         # Mean reversion speed
	sigma_r = 0.015, # Volatility of short rate
	
	# 2. Market Forward Curve
	forward_curve_dates = [0, 1, 2, 3, 5],
	forward_curve_rates = [0.0435, 0.040, 0.038, 0.035, 0.035],
    
    	# 3. Asset Parameters
    	# Note: House drift mu_L is often modeled as (r_t + risk_premium)
    	# But for simplicity, we keep constant risk premia relative to the Simulated Rate
    	risk_premium_D = 0.045, # Domestic Equity Premium
    	risk_premium_G = 0.045, # Global Equity Premium
    	risk_premium_L = 0.020, # Housing Risk Premium
    
    	sigma_D = 0.18, sigma_G = 0.15, sigma_L = 0.10,
    
    	# 4. Allocation
    	w_D = 0.50
):
    w_G = 1 - w_D
    n_steps = int(n_years / dt)
    time_grid = np.linspace(0, n_years, n_steps + 1)
    
    # --- Interpolate Forward Curve ---
    # f(0, t) represents the market's expectation of future instantaneous rates
    f_0_t = interp1d(forward_curve_dates, forward_curve_rates, kind='linear', fill_value="extrapolate")
    
    # Pre-calculate Theta(t) for Hull-White
    # theta(t) = df/dt + a*f(0,t) + (sigma^2 / 2a)*(1 - exp(-2at))
    # Approximation: For simulation, we can model r(t) = x(t) + alpha(t)
    # where x(t) is a zero-mean OU process, and alpha(t) fits the term structure.
    
    # Correlation Matrix (Same logic as before)
    # Rate, Domestic, Global, House
    corrs = np.array([
        [ 1.0, -0.4, -0.1, -0.6], 
        [-0.4,  1.0,  0.6,  0.4], 
        [-0.1,  0.6,  1.0,  0.1], 
        [-0.6,  0.4,  0.1,  1.0] 
    ])
    L_chol = np.linalg.cholesky(corrs)
    
    # Storage
    r = np.zeros((n_scenarios, n_steps + 1))
    S_D = np.zeros((n_scenarios, n_steps + 1))
    S_G = np.zeros((n_scenarios, n_steps + 1))
    L = np.zeros((n_scenarios, n_steps + 1))
    
    # Initialize
    r[:, 0] = f_0_t(0)
    S_D[:, 0] = 100; S_G[:, 0] = 100; L[:, 0] = 100
    
    # Calculate deterministic shift alpha(t) to match forward curve
    # Analytical result for alpha(t) in Hull-White:
    # alpha(t) = f(0,t) + (sigma_r**2 / (2*a**2)) * (1 - np.exp(-a*t))**2
    # We will use this to center the simulation.
    
    for t_idx in range(n_steps):
        t = time_grid[t_idx]
        dt_val = dt
        
        # 1. Generate Shocks
        Z = np.random.normal(0, 1, (n_scenarios, 4))
        dW = Z @ L_chol.T * np.sqrt(dt_val)
        
        dW_r = dW[:, 0]
        dW_D = dW[:, 1]
        dW_G = dW[:, 2]
        dW_L = dW[:, 3]
        
        # 2. Update Short Rate (Hull-White discretization)
        # We simulate the process x(t) = r(t) - alpha(t) which is OU mean-reverting to 0
        # But simpler: r(t+dt) = r(t) + [theta(t) - a*r(t)]dt + sigma*dW
        
        # Calculate theta(t) roughly numerically from forward curve slope
        f_t = f_0_t(t)
        f_t_next = f_0_t(t + dt)
        df_dt = (f_t_next - f_t) / dt
        
        # Hull-White drift term
        theta_t = df_dt + a * f_t + (sigma_r**2 / (2*a)) * (1 - np.exp(-2*a*t))
        
        current_r = r[:, t_idx]
        dr = (theta_t - a * current_r) * dt + sigma_r * dW_r
        r[:, t_idx+1] = current_r + dr
        
        # 3. Update Assets
        # Crucial: The DRIFT of assets depends on the CURRENT Rate r(t)
        # This creates the "Duration" effect mechanically.
        
        # Domestic Equity: Drift = r(t) + RiskPremium
        mu_D_t = r[:, t_idx] + risk_premium_D
        S_D[:, t_idx+1] = S_D[:, t_idx] * np.exp((mu_D_t - 0.5*sigma_D**2)*dt + sigma_D*dW_D)
        
        # Global Equity: Drift = r(t) + RiskPremium 
        # (Assumption: Unhedged global returns drift with local r if we assume UIP holds loosely, 
        # or we just assume constant global drift. Let's use constant global drift to differentiate).
        # Actually, for an Australian investor, Global drift = r_AUD + Global_Premium (hedged) 
        # or r_USD + Global_Premium + FX_Change (unhedged).
        # Let's assume simple CAPM: Drift = RiskFree + Premium
        mu_G_t = r[:, t_idx] + risk_premium_G
        S_G[:, t_idx+1] = S_G[:, t_idx] * np.exp((mu_G_t - 0.5*sigma_G**2)*dt + sigma_G*dW_G)
        
        # House: Drift = r(t) + RiskPremium (or r(t) - RentalYield...)
        # A simpler way: House prices react to rate *changes* via correlation (which we have)
        # and drift with the rate (inflationary component).
        mu_L_t = r[:, t_idx] + risk_premium_L
        L[:, t_idx+1]   = L[:, t_idx]   * np.exp((mu_L_t - 0.5*sigma_L**2)*dt + sigma_L*dW_L)

    # Output
    Portfolio = w_D * S_D[:, -1] + w_G * S_G[:, -1]
    Funding_Ratio = Portfolio / L[:, -1]
    return Funding_Ratio

# Compare Strategies
fr_50 = simulate_hull_white(w_D=0.50)
fr_00 = simulate_hull_white(w_D=0.00) # 100% Global

print(f"Hull-White Results (Forward Curve: Inverted 4.35% -> 3.5%)")
print(f"50/50 Strategy Std Dev: {np.std(fr_50):.4f}")
print(f"Global Strategy Std Dev: {np.std(fr_00):.4f}")
