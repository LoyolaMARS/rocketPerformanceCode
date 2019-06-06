def alt2pres(altitude):
    '''
    Determine site pressure from altitude.

    Parameters
    ----------
    altitude : numeric
        Altitude in meters above sea level

    Returns
    -------
    pressure : numeric
        Atmospheric pressure (Pascals)

    Notes
    ------
    The following assumptions are made
    
    - Hydrostatic equilibrium
    - Perfect gas
    - Gravity independent of altitude
    - Constant lapse rate

    ============================   ================
    Parameter                      Value
    ============================   ================
    Base pressure                  101325 Pa
    Temperature at zero altitude   288.15 K
    Gravitational acceleration     9.80665 m/s^2
    Lapse rate                     -6.5E-3 K/m
    Gas constant for air           287.053 J/(kgK)
    Relative Humidity              0%
    ============================   ================
    
    Reviewed and repurposed for Loyola MARS Base11 by Max Fung (1-24-2019)

    References
    -----------
    [1] "A Quick Derivation relating altitude to air pressure" from
    Portland State Aerospace Society, Version 1.03, 12/22/2004.
    https://www.researchgate.net/file.PostFileLoader.html?id=5409cac4d5a3f2e81f8b4568&assetKey=AS%3A273593643012096%401442241215893
    [2] "Source Code for pvlib.atmosphere" from ReadTheDocs.io, 1/23/2019.
    https://pvlib-python.readthedocs.io/en/latest/_modules/pvlib/atmosphere.html
    '''

    '''
    Derived Equation:
        
        altitude = T0/L*((P/P0)**(-L*R/g)-1)
        
        P0 - pressure at zero altitude (base pressure)
        T0 - temperature at zero altitude
        g - acceleration due to gravity
        L - lapse rate
        R - gas constant for air
        Rh - relative humidity
        
        Note - L near the ground is a negative number
    '''

    press = 100 * ((44331.514 - altitude) / 11880.516) ** (1 / 0.1902632)
    press = press / 6894.75729 # Pa to psi

    return press