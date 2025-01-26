# Q&A

- How do I save & load multiple meshes/labels to my STL file?
    - It is not possible to save multiple meshes in a single STF file. Each mesh must be store in a separate file. The code below shows how to save all the meshes and use their labels (unique ID) as a base for their file names.
      ```python
      STL_path = "where_do_you_want_to_save_the_STL_files";
      
      list_of_meshes = ["root"];

      while len(list_of_meshes):
        label = list_of_meshes.pop(0);
        if gvxr.getNumberOfPrimitives(label):
          gvxr.saveSTLfile(label, os.path.join(STL_path, label + ."stl");

        for i in range(gvxr.getNumberOfChildren(label)):
          list_of_meshes.append(gvxr.getChildLabel(label, i));
      ```
      
    - 


- My sample consists of different components made from different materials. I've created a .stl 3D model of my sample. How can I assign different materials to different parts of the 3D model via gVXR?