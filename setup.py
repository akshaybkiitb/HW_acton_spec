from setuptools import setup

setup(
    name = 'ScopeFoundryHW.acton_spec',
    
    version = '0.0.1',
    
    description = 'ScopeFoundry Hardware plug-in: Acton spectrometer',
    
    # Author details
    author='Edward S. Barnard',
    author_email='esbarnard@lbl.gov',

    # Choose your license
    license='BSD',

    package_dir={'ScopeFoundryHW.acton_spec': '.'},
    
    packages=['ScopeFoundryHW.acton_spec',],
        
    package_data={
        '':["README*", 'LICENSE', # include License and readme 
            "*.ui", # include QT ui files 
            ], 
        },
    )
