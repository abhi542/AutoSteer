import os, h5py

def inspect_h5_file(file_path):
    with h5py.File(file_path, 'r') as f:
        def print_attrs(name, obj):
            print(name)
            for key, val in obj.attrs.items():
                print(f"    {key}: {val}")

        f.visititems(print_attrs)

model_path = os.path.join('Autopilot/models', 'Autopilot.h5')
inspect_h5_file(model_path)