from netCDF4 import Dataset

# Open the NetCDF file
nc_file = 'Total_Curvature.nc'
nc_data = Dataset(nc_file, 'r')

# Access variables and their data
for var_name, var in nc_data.variables.items():
    print("Variable:", var_name)
    print("Data:", var[:])  # Accessing data from the variable
