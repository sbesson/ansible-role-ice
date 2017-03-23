Role Name
=========

Install Zeroc Ice.


Role Variables
--------------

Required:
- `ice_version`: The Ice version, either 3.5 or 3.6


Notes
-----
Note that 3.6 requires ice-python to be installed using pip, and will result in the installation of several development tools and libraries.
The pip version is required in major.minor.patch form so `vars/ice-3.6.yml` will need to be updated whenever there is a new patch release.


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
