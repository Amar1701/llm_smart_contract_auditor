# File: parser/solidity_parser.py

from solcx import compile_standard, install_solc
import os

class SolidityParser:
    def __init__(self, solc_version="0.8.20"):
        install_solc(solc_version)
        self.solc_version = solc_version

    def parse(self, contract_path):
        if not os.path.exists(contract_path):
            raise FileNotFoundError(f"Contract not found: {contract_path}")

        with open(contract_path, "r") as file:
            source_code = file.read()

        compiled = compile_standard(
            {
                "language": "Solidity",
                "sources": {
                    "Contract.sol": {
                        "content": source_code
                    }
                },
                "settings": {
                    "outputSelection": {
                        "Contract.sol": {
                            "": ["ast"],                 # ✅ FILE-LEVEL AST
                            "*": ["abi", "evm.bytecode"] # ✅ CONTRACT-LEVEL OUTPUTS
                        }
                    }
                }
            },
            solc_version=self.solc_version,
        )

        ast = compiled["sources"]["Contract.sol"]["ast"]

        return {
            "source": source_code,
            "ast": ast
        }
