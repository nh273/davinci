

init : directories files

define structure
Built structure :
----------------------
| -src/
| -notebooks/
| -results/
| -docs/
| -data/
|   | -- raw/
|   | -- intermediary/
|   | -- external/
|   | -- processed/
----------------------
endef
export structure

define ignore
\n
data/raw/*
data/intermediary/*
data/processed/*
results/*
endef
export ignore

define blank_notebook
{
	"cells": [],
	"metadata": {
		"language_info": {
			"codemirror_mode": {
				"name": "ipython",
				"version": 3
				},
			"file_extension": ".py",
			"mimetype": "text/x-python",
			"name": "python",
			"nbconvert_exporter": "python",
			"pygments_lexer": "ipython3",
			"version": "3.6.5"
			}
		},
	"nbformat": 4,
	"nbformat_minor": 2
}
endef
export blank_notebook

directories :
	@[ -d src ] || mkdir src
	@[ -d notebooks ] || mkdir notebooks
	@[ -d docs ] || mkdir docs
	@[ -d data ] || mkdir data
	@[ -d results ] || mkdir results
	@[ -d data/processed ] || mkdir data/processed
	@[ -d data/raw ] || mkdir data/raw
	@[ -d data/external ] || mkdir data/external
	@[ -d data/intermediary ] || mkdir data/intermediary
	@echo "$$structure"

files :
	@[ -f main.ipynb ] || touch main.ipynb
	@[ -f README.md ] || touch README.md
	@[ -f .gitignore ] || touch .gitignore
	@echo "$$blank_notebook" >> main.ipynb
	@echo "$$ignore" >> .gitignore
	@echo "Created main.ipynb"
	@echo "Created .gitignore"
	@echo "	> ignores data/processed/*, data/raw/*, data/intermediary/*, results/*"

clean :
	@rm -f data/raw/*
	@rm -f data/processed/*
	@rm -f data/intermediary/*
	@rm -f results/*
	@echo "Deleted all files from raw, intermediary, processed and results"
