import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python3.11", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}: {e}")

if __name__ == "__main__":
    while True:
        # Preguntar al usuario si desea enlazar el corpus
        enlazar_corpus = input("Linkar Corpus? (Y/n): ").strip().lower()

        if enlazar_corpus == 'y':
            # Ejecutar unifiedCorpus.py
            run_script("unifiedCorpus.py")

            # Ejecutar unifiedIterator.py
            run_script("unifiedIterator.py")
        else:
            # Preguntar al usuario si desea generar el Local Minimum
            generate_local_minimum = input("Generate Local Minumun? (Y/n): ").strip().lower()

            if generate_local_minimum == 'y':
                # Ejecutar refinement.py
                run_script("refinement.py")
            else:
                # Preguntar al usuario si desea salir del programa
                exit_program = input("Exit? (Y/n): ").strip().lower()

                if exit_program == 'y':
                    break
