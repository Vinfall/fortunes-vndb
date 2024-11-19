# Varables
PYTHON = python
PIP = pip
SUDO = sudo

# Dependencies & scripts

run: ## get vndb quotes
	$(PIP) format.py

clean: ## clean up outputs
	-rm output/vndb*

install: output/vndb ## install vndb fortunes
	@echo "Installing VNDB quotes to fortunes database..."
	$(SUDO) install -pm644 ./output/vndb* /usr/share/fortunes/

test: ## get random VNDB quote
	fortune vndb

uninstall: ## remove vndb quotes from fortunes
	@echo "Removing VNDB quotes from fortunes database..."
	$(SUDO) rm /usr/share/fortunes/vndb /usr/share/fortunes/vndb.dat

help: ## show this help
	@echo "Specify a command:"
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[0;36m%-12s\033[m %s\n", $$1, $$2}'
	@echo ""
.PHONY: help
