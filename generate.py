import os
import shutil

print("""
 ██▀███  ▓█████ ▄▄▄       ▄████▄  ▄▄▄█████▓
▓██ ▒ ██▒▓█   ▀▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒
▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░
▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ 
░██▓ ▒██▒░▒████▒▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ 
░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   
  ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░  ░  ▒       ░    
  ░░   ░    ░    ░   ▒   ░          ░      
   ░        ░  ░     ░  ░░ ░               
                         ░                 
""")
print("""
  ╔═╗┌─┐┬ ┬┬─┐┌─┐┬  ┬  ╔═╗┬ ┬┌┬┐┌─┐┌┬┐
  ╚═╗│ ││ │├┬┘├─┤└┐┌┘  ╠═╣├─┤│││├┤  ││
  ╚═╝└─┘└─┘┴└─┴ ┴ └┘   ╩ ╩┴ ┴┴ ┴└─┘─┴┘
  Author: Sourav Ahmed
  Author-Github: https://github.com/b33lz3bubTH
""")


_project_name: str = input("Enter Project Name: (Eg - research) - ")
_port:int = int(input("Enter Project Port: (Eg - 3001) - "))


_cracorc_file = ".cracorc.js"
_craco_rc_JS = f"""
const {{ ModuleFederationPlugin }} = require("webpack").container;
const deps = require("./package.json").dependencies;
module.exports = () => ({{
    webpack: {{
      configure: {{
        output: {{
          publicPath: "auto",
        }},
      }},
      plugins: {{
        add: [
          new ModuleFederationPlugin({{
            name: "{_project_name.lower()}",
            filename: "remoteEntry.js",
            exposes: {{
            "./ResearchPage": "./src/pages/researchPage.jsx"
            }},
            remotes: {{

            }},
            shared: {{
              ...deps,
              ui: {{
                singleton: true,
              }},
              react: {{
                singleton: true,
                requiredVersion: deps.react,
              }},
              "react-dom": {{
                singleton: true,
                requiredVersion: deps["react-dom"],
              }},
            }},
          }}),
        ],
      }},
    }},
  }});
"""

_package_file = "package.json"
_package_JSON = f"""
{{
  "name": "{_project_name}",
  "version": "0.1.0",
  "private": true,
  "dependencies": {{
    "@testing-library/jest-dom": "^5.16.4",
    "@testing-library/react": "^13.3.0",
    "@testing-library/user-event": "^13.5.0",
    "@types/jest": "^27.5.2",
    "@types/node": "^16.11.45",
    "@types/react": "^18.0.15",
    "@types/react-dom": "^18.0.6",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "typescript": "^4.7.4",
    "ui": "*",
    "web-vitals": "^2.1.4"
  }},
  "scripts": {{
    "dev": "DISABLE_ESLINT_PLUGIN=true PORT={_port} craco start",
    "build": "craco build",
    "test": "craco test",
    "eject": "craco eject"
  }},
  "eslintConfig": {{
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  }},
  "browserslist": {{
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }},
  "devDependencies": {{
    "@craco/craco": "^6.4.5"
  }}
}}
"""

_index_file = "public/index.html"
_index_HTML = f"""
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8" />
      <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <meta name="theme-color" content="#000000" />
      <meta
        name="{_project_name}"
        content="Web site created using create-react-app"
      />
      <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
      <!--
        manifest.json provides metadata used when your web app is installed on a
        user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
      -->
      <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
      <!--
        Notice the use of %PUBLIC_URL% in the tags above.
        It will be replaced with the URL of the `public` folder during the build.
        Only files inside the `public` folder can be referenced from the HTML.

        Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
        work correctly both with client-side routing and a non-root public URL.
        Learn how to configure a non-root public URL by running `npm run build`.
      -->
      <title>{_project_name}</title>
    </head>
    <body>
      <noscript>You need to enable JavaScript to run this app.</noscript>
      <div id="root"></div>
      <!--
        This HTML file is a template.
        If you open it directly in the browser, you will see an empty page.

        You can add webfonts, meta tags, or analytics to this file.
        The build step will place the bundled scripts into the <body> tag.

        To begin the development, run `npm start` or `yarn start`.
        To create a production bundle, use `npm run build` or `yarn build`.
      -->
    </body>
  </html>
"""


# (file_name, file_content)
project_folder_setup = [ 
  (_cracorc_file, _craco_rc_JS),
  (_index_file, _index_HTML),
  (_package_file, _package_JSON)
]

current_directory = os.getcwd()
project_root = os.path.dirname(os.path.abspath(__file__))
project_root_react_project_name = "react-mfe-app"

print("Current Dir: ", current_directory)
print("Project Dir: ", f"{project_root}/{project_root_react_project_name}")

shutil.copytree(f"{project_root}/{project_root_react_project_name}", f"{current_directory}/{_project_name.lower()}", 
            symlinks=False, ignore=None, 
            ignore_dangling_symlinks=False, 
            dirs_exist_ok=False)


project_folder = f"{current_directory}/{_project_name.lower()}"
for file_name, content in project_folder_setup:
  file_descriptor = open(f"{project_folder}/{file_name}", "a")
  file_descriptor.write(content)
  file_descriptor.close()



print(f"""
Note:
  - Project is based on react typescript.
  - cd {_project_name.lower()} && ( yarn install or npm install ) to install dependencies.
  - go berserk break the code.
""")
