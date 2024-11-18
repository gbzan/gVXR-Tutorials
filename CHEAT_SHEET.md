# Cheat sheet: Quick help of all gVXR's functions used in the tutorial notebooks

- `gvxr.getVersionOfCoreGVXR`:
  - Description: Accessor on the full string version of the core gVirtualXRay library (gvxr).  
  - Called in file: test_installation.ipynb
    - At Cell: [7]


- `gvxr.getVersionOfSimpleGVXR`:
  - Description: Accessor on the full string version of SimpleGVXR.  
  - Called in file: test_installation.ipynb
    - At Cell: [8]


- `gvxr.createNewContext`:
  - Description: Create an OpenGL context.  
  - Called in file: test_installation.ipynb
    - At Cell: [8]


- `gvxr.terminate`:
  - Description: Close and destroy all the windows and OpenGL contexts that have been created.
  - Called in file: test_installation.ipynb
    - At Cell: [11]

  - Called in file: first_xray_simulation.ipynb
    - At Cell: [17]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [22]


- `gvxr.createOpenGLContext`:
  - Description: Create an OpenGL context (the window won't be shown).  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [5]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [7]


- `gvxr.setSourcePosition`:
  - Description: Set the position of the X-ray source.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [6]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [8]


- `gvxr.usePointSource`:
  - Description: Use a point source, i.e. a cone-beam geometry.
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [6]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [8]


- `gvxr.setMonoChromatic`:
  - Description: Use a monochromatic beam spectrum (i.e. one single energy).  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [7]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [9]


- `gvxr.setDetectorPosition`:
  - Description: Set the position of the X-ray detector.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [8]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [10]


- `gvxr.setDetectorUpVector`:
  - Description: Set the up-vector defining the orientation of the X-ray detector.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [8]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [10]


- `gvxr.setDetectorNumberOfPixels`:
  - Description: Set the number of pixels of the X-ray detector.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [8]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [10]


- `gvxr.setDetectorPixelSize`:
  - Description: Set the pixel size. Same as the function setDetectorPixelPitch.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [8]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [10]


- `gvxr.loadMeshFile`:
  - Description: Load a polygon mesh from a file, set its label in the scenegraph (i.e.
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [9]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [11]


- `gvxr.moveToCentre`:
  - Description: Move a polygon mesh to the centre.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [9]


- `gvxr.setElement`:
  - Description: Set the chemical element (or element) corresponding to the material properties
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [10]


- `gvxr.setCompound`:
  - Description: Set the compound corresponding to the material properties of a polygon mesh.
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [10]


- `gvxr.setDensity`:
  - Description: Set the density corresponding to the material properties of a polygon mesh.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [10]


- `gvxr.setMixture`:
  - Description: Set the mixture corresponding to the material properties of a polygon mesh.
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [10]


- `gvxr.computeXRayImage`:
  - Description: Compute the X-ray projection corresponding to the environment that has
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [11]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [12]


- `gvxr.displayScene`:
  - Description: 3-D visualisation of the 3-D scene (source, detector, and scanned objects). Note
  - Called in file: first_xray_simulation.ipynb
    - At Cells: [11, 14]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cells: [12, 15, 18]


- `gvxr.saveLastXRayImage`:
  - Description: Save the last X-ray image that has been computed.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [12]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [13]


- `gvxr.saveLastLBuffer`:
  - Description: Save the last L-buffer, i.e. path length, that has been computed.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [12]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [13]


- `gvxr.setColour`:
  - Description: Set the colour of a given polygon mesh. It will be applied to the ambiant,
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [14]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [11]


- `gvxr.setWindowBackGroundColour`:
  - Description: Set window background colour.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [14]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [15]


- `gvxr.takeScreenshot`:
  - Description: Take screenshot.  
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [15]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cells: [16, 18]


- `gvxr.renderLoop`:
  - Description: 3-D visualisation of the 3-D scene (source, detector, and scanned objects). Note
  - Called in file: first_xray_simulation.ipynb
    - At Cell: [16]

  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [19]


- `gvxr.removePolygonMeshesFromXRayRenderer`:
  - Description: Empty the X-ray renderer from all its meshes. Note that the meshes are kept in
  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [11]


- `gvxr.emptyMesh`:
  - Description: Create an empty polygon mesh and set its label in the scenegraph (i.e.
  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [11]


- `gvxr.setHounsfieldUnit`:
  - Description: Set the Hounsfield value corresponding to the material properties of a polygon
  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [11]


- `gvxr.scaleNode`:
  - Description: Scale a polygon mesh.  
  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [11]


- `gvxr.getZoom`:
  - Description: ***** MISSING *****
  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cells: [17, 19]


- `gvxr.getSceneRotationMatrix`:
  - Description: ***** MISSING *****
  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cells: [17, 19]


- `gvxr.setZoom`:
  - Description: ***** MISSING *****
  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [18]


- `gvxr.setSceneRotationMatrix`:
  - Description: ***** MISSING *****
  - Called in file: multi_material-lungman_phantom.ipynb
    - At Cell: [18]