# This is a script for the MedHist Project.
#
# Given:
# (1) An (incomplete) db export of image names (id), years of creation and authors.
# (2) A folder (Data/imgs) full of images named by id. Some id_subimages exist, which aren't listed in (1) yet.
#
# Goal:
# (1) Sort images in folder by year with the following steps
#
# Approach:
# (1) complete given list of images (1)
# (2) rename images in folder to year_author_id
# (3) reupload new folder for requesting person


from os import listdir
import pandas as pd


# Load image names in list
img_path = "Data/imgs"
file_list = [f for f in listdir(img_path)]
no_ext_list = [x.split('.')[0] for x in file_list]
# print(file_list)
print(no_ext_list)
print(len(no_ext_list))

inv_nr = no_ext_list
datierung = ["-"] * len(no_ext_list)
kuenstler = ["-"] * len(no_ext_list)
aux_dict = {"Inv.Nr.": inv_nr, "Datierung": datierung, "Künstler": kuenstler}

img_folder_df = pd.DataFrame(aux_dict)
# img_folder_df = pd.DataFrame(no_ext_list, columns=["Inv.Nr.", "Datierung", "Künstler"])
print(img_folder_df)


# Load excel list using pandas data frame
dbinfo_df = pd.read_excel (r'Data\Medhist_Invnr_Dat_Kuenstler.xlsx')
print (dbinfo_df)

merged_df = pd.merge(dbinfo_df, img_folder_df, on="Inv.Nr.", how="outer")
print(merged_df)

merged_df.to_csv("Data/merged_output.csv", sep=";", encoding='utf-8')
