import nle.dataset as nld

def main():
    path_to_nld_aa = "/efs/tuylsjen/NLD-AA"
    path_to_nld_nao = "/efs/tuylsjen/NLD_NAO"
    path_to_custom = "/path/to/a/custom/nledata/directory"

    # Chose a database name/path. By default, most methods with use nld.db.DB (='ttyrecs.db')
    dbfilename = "ttyrecs.db"
    if not nld.db.exists(dbfilename):
        nld.db.create(dbfilename)
            
        # To add the NLE-AA data, or any data generated from nle, use `add_nledata_directory`.
        nld.add_nledata_directory(path_to_nld_aa, "nld-aa", dbfilename)

        # to add the NLE-NAO data, use the `add_altorg_directory`.
        nld.add_altorg_directory(path_to_nld_nao, "nld-nao", dbfilename) 
        
        # To add a custom NLE directory, as above, use `add_nledata_directory`.
        # nld.add_nledata_directory(path_to_custom, "custom_name", dbfilename)

if __name__ == "__main__":
    main()