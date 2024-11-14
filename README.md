# Hands-on training: Simulating X-ray images on GPU with ![[gVirtualXray (gVXR)](https://gvirtualxray.sourceforge.io/)](img/Logo-transparent-small.png) 

## Content of this file

- Installation
    - Using Conda
    - Using pip
- Content of this repository
    - [Test installation](notebooks/test_installation.ipynb) 
    - [First X-ray simulation](notebooks/first_xray_simulation.ipynb)
- How to find help
- How to cite
- Research excellence
- User contributions
      
## Installation

### Using Conda

```bash
conda env create -f environment.yml
conda activate gvxr-tutorials
```

### Using pip

```bash
pip install gvxr
pip install matplotlib viewscad xpecgen
pip install git+https://bitbucket.org/spekpy/spekpy_release.git
```

## Content of this repository

- [Test installation](notebooks/test_installation.ipynb): Run the quick test script provided with gVirtualXray's Python package to make sure the installation is working well on your system. <a href="https://colab.research.google.com/github/TomographicImaging/gVXR-Tutorials/blob/main/notebooks/test_installation.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
- [First X-ray simulation](notebooks/first_xray_simulation.ipynb): Explore the step-by-step notebook to create our first X-ray radiograph. A mono-material object is imaged with a monochromatic source and an ideal detector. We show how to visualise the X-ray radiograph and take a screenshot of the 3D visualisation of the simulation environment. <a href="https://colab.research.google.com/github/TomographicImaging/gVXR-Tutorials/blob/main/notebooks/first_xray_simulation.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## How to find help

- Email me (Franck P. Vidal, STFC);
- Raise an issue on GitHub: [https://github.com/TomographicImaging/gVXR-Tutorials/issues](https://github.com/TomographicImaging/gVXR-Tutorials/issues)
- Open a ticket on SourceForge: [https://sourceforge.net/p/gvirtualxray/tickets](https://sourceforge.net/p/gvirtualxray/tickets);
- Use the forum on SourceForge: [https://sourceforge.net/p/gvirtualxray/discussion/](https://sourceforge.net/p/gvirtualxray/discussion/);
- Subscribe to the mailing list: [https://sourceforge.net/projects/gvirtualxray/lists/gvirtualxray-discuss](https://sourceforge.net/projects/gvirtualxray/lists/gvirtualxray-discuss)
- Check the technical documentation, e.g. calling `help(gvxr)` for help on the Python package or something like `help(gvxr.createNewContext)` for a specific function.

## How to cite

If you use gVXR in your own applications, particularly for research & development, I will be grateful if you could cite the articles as follows:

- **Seminal paper**: Vidal, F. P., Garnier, M., Freud, N., Létang, J. M., and John, N. W., “Simulation of x-ray attenuation on the GPU,” in [Proceedings of Theory and Practice of Computer Graphics 2009](https://diglib.eg.org/collections/916dfc7f-8278-428f-9ae3-c85aeff29595), 25–32, [Eurographics Association](https://www.eg.org/), Cardiff, UK (June 2009). DOI: [10.2312/LocalChapterEvents/TPCG/TPCG09/025-032](https://doi.org/10.2312/LocalChapterEvents/TPCG/TPCG09/025-032)
- **First reference to gVXR as an opensource software**: Vidal, F. P. and Villard, P.-F., “Development and validation of real-time simulation of x-ray imaging with respiratory motion,” Computerized Medical Imaging and Graphics 49, 1–15 (2016). DOI: [10.1016/j.compmedimag.2015.12.002](https://doi.org/10.1016/j.compmedimag.2015.12.002)
- **Clinical validation study**: Pointon, J. L., Wen, T., Tugwell-Allsup, J., Sújar, A., Létang, J. M., and Vidal, F. P., “Simulation of x-ray projections on gpu: Benchmarking gvirtualxray with clinically realistic phantoms,” Computer Methods and Programs in Biomedicine 234, 107500 (2023). DOI: [10.1016/j.cmpb.2023.107500](https://doi.org/10.1016/j.cmpb.2023.107500)
- **Review paper on CT applications**: Vidal, F. P., Afshari, S., Ahmed, S., Atkins, C. Béchet, E., Bellot, A., Bosse, S., Chahid, Y., Chou, C.-Y., Culver, R., Dixon, L., Friemann, J., Garbout, A., Hatton, C., Henry, A., Leblanc, C., Leonardi, A., Létang, J. M., Lipscomb, H., Manchester, T., Meere, B., Middleburgh, S., Mitchell, I., Perera, L., Puig, M., and Tugwell-Allsup, J., “X-ray simulations with gVXR as a useful tool for education, data analysis, set-up of CT scans, and scanner development,” in [Developments in X-Ray Tomography XV, SPIE Optics & Photonics](https://doi.org/10.1117/12.3025315), Volume 13152, [SPIE](https://spie.org/), San Diego, California, United States (Aug 2024). DOI: [10.1117/12.3025315](https://doi.org/10.1117/12.3025315)

## User contributions on our website

We'd like to share user contributions in a new section of gVXR's website [https://gvirtualxray.sourceforge.io/](https://gvirtualxray.sourceforge.io/). If you'd like to showcase your work, please contact me by email (Franck P. Vidal, STFC) or raise an issue on GitHub ([https://github.com/TomographicImaging/gVXR-Tutorials/issues](https://github.com/TomographicImaging/gVXR-Tutorials/issues)).



<!--
- Session 1
    - [Notebook 0](00-warming-up.ipynb) -- Warming up
        - Log in;
        - Copy the training data;
        - Install the Python packages needed for this course;
        - Check that [gVirtualXray](https://gvirtualxray.sourceforge.io/) is working well;
        - Verify which version of [gVirtualXray](https://gvirtualxray.sourceforge.io/) is installed (software and hardware);
        - How to get help (during and after the training).
    - [Notebook 1](01-Introduction-to-Xray-attenuation.ipynb) -- Introduction to X-ray attenuation and its implementation in [gVirtualXray](https://gvirtualxray.sourceforge.io/)
        - Explain what gVXR is and why it has been developed;
        - Introduce projection X-ray imaging and how X-rays are produced;
        - Understand how X-rays interact with matter;
        - Become familiar with the Beer-Lambert law to compute the attenuation of X-rays by matter;
        - Describe how the Beer-Lambert law is implemented in [gVirtualXray](https://gvirtualxray.sourceforge.io/);
        - Compare images simulated using [gVirtualXray](https://gvirtualxray.sourceforge.io/) with ground truth images.
- Session 2
    - [Notebook 2](02-first_xray_simulation.ipynb) -- First X-ray radiograph simulations
        - Create our first X-ray simulation, step-by-step;
        - Save our X-ray image in a file format that preserves the original dynamic range;
        - Visualise the results with 3 different look-up tables;
        - Visualise the 3D environment.
    - [Notebook 3](03-multi_material_sample.ipynb) -- Multi-material samples
        - Chemical elements
        - Mixtures
        - Compounds
- Session 3
    - [Notebook 4](04-source_parameters.ipynb) -- Source types and paramaters
        - Parallel beam (synchrotron)
        - Cone-beam (X-ray tube)
        - Focal spot
        - Polychromatic spectrum
        - Pixel size, magnification
    - Preview: watch out for new release with photonic noise model
    - [Notebook 5](05-detector_parameters.ipynb) -- Detector paramaters
        - Pixel size (revisited)
        - Point spread function
        - Energy response of the detector
- Session 4
    - [Notebook 6](06-CT_acquisition.ipynb) -- Simulating CT scans
        - Parallel beam
        - Cone beam
        - Monochromatic spectrum
        - Polychromatic spectrum
    - [Notebook 7](07-2D_registration_Xray_radiograph.ipynb) -- Using simulations for image registration
<!--     - [Notebook 8](08-3D_registration_Xray_CT.ipynb) -->
<!--


- 12:30 – Lunch
- 13:30 – Session 3 (1 hour 15 minutes)
    - gVXR: More advanced simulations
            - Polychromatic spectrum  (faut parler de l'influence des kV et mA, de l'utilisation de filtres et du type d'anode (W, Mo, Cu...).)  Pour le 5 et 8, il serait bien de montrer à exposition constante (mAs) l'influence de la taille du pixel.
            - Photonic noise
- 14:45 – Coffee
- 15:15 – Session 4 (1 hour 45 minutes)
    - gVXR: Simulation of tomography acquisition
        1. parallel
        2. cone beam
        3. monochromatic
        4. polychromatic
        5. noisy
        6. noiseless
    - gVXR: Image registration
- 17:00 – End -->