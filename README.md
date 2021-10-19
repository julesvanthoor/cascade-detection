# cascade-detection

The code belonging to this thesis is split into 5 jupyter notebooks:

**DetectCascades**: the main file, which computes system-level events, cascades, frequent paths, etc. It uses (almost all the other files)
**Events**: contains functionality for computing system-level events, cascades, frequent paths
**Thresholds**: contains all functionality for computing thresholds (including jenks)
**Plotting**: contains all functionality regarding plotting performance spectra
**PlotPerformanceSpectrum**: in this notebook, some example plots are shown. Uses the Plotting notebook

In addition to this, there are 2 Python files which are used by the notebooks:

**Constants.py**: contains all constants (segments, abbreviations, etc) used trhoughout the project
**PerformanceSpectrum.py**: contains all code needed to plot a performance spectrum (almost completely derived from Tom van Meers work: https://github.com/tomvmeer/PF4PY)
