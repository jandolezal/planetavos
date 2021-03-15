# Planeta vos

[![Netlify Status](https://api.netlify.com/api/v1/badges/42ae717d-1021-44c8-bfc4-a74909599f7a/deploy-status)](https://app.netlify.com/sites/planetavos/deploys)

Blog [Planeta vos](https://www.planetavos.cz), připravený s pomocí [Pelican](https://getpelican.com/) a [Jinja](https://palletsprojects.com/p/jinja/).

Hostovaný na Netlify, kde se publikuje adresář `output` vytvořený příkazem `pelican content -s publishconf.py` po každé změně v tomto repozitáři. Stačilo [nastavit](https://docs.netlify.com/configure-builds/manage-dependencies/#python) proměnnou prostředí PYTHON_VERSION a nezapomenout na `requirements.txt`.
