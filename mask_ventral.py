masker = NiftiMasker(haxby_data.mask_vt[0])
X = masker.fit_transform(func_file)

