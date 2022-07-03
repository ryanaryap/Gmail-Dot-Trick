import typer
from email import dot_trick
def main(email_address: str, output_file: str):
    iterations = dot_trick(email_address)
    typer.echo("Saving emails to text...")
    with typer.progressbar(iterations) as progress:
        with open(output_file, "w+") as file:
            for email in progress:
                file.write(f'{email}\n')
    typer.echo("Done!")
    
if __name__ == "__main__":
    typer.run(main)