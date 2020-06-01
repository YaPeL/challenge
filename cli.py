from challenge import GitExtractor

if __name__ == "__main__":
    properties = ["id", "objects[0].name", "objects[0].kill_chain_phases"]
    ge = GitExtractor(repo="https://github.com/mitre/cti",
                      folder='enterprise-attack/attack-pattern',
                      props=properties)
    for file, result in ge.files():
        print(f"For file {file} extracted:")
        print(result)
