"""
NPX-PDF-BRASIL
Portfolio integration script

Author: Natalia Barros
Description:
Adds and documents the NPX-PDF-BRASIL project into the Python portfolio.
"""

def add_project():
    project = {
        "name": "NPX-PDF-BRASIL",
        "type": "SaaS MVP",
        "stack": ["Python", "PDF Processing"],
        "market": "Brazil"
    }
    return project


if __name__ == "__main__":
    print(add_project())
