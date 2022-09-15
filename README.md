## Welcome Friend,
***

### This is best fit for turborepo.

> Setup

    -- git clone git@github.com:b33lz3bubTH/react-microfrontend-generator.git /tmp/react-microfrontend-generator
    -- go to your mono repo or mfes folder
    -- ** python3 /tmp/react-microfrontend-generator/generate.py **



> Demo Video
> 
[![Youtube Preview](https://img.youtube.com/vi/Rb5KXQ573ho/0.jpg)](https://www.youtube.com/watch?v=Rb5KXQ573ho)



## Microfrontend In Monorepos


-- Mono Repo Setup For Shared Libs

    1. installing Dependensices
            on (my-resume/packages/ui)
            yarn install rxjs

    2. new mfe-apps
            - on (my-resume/apps)
            - npx create-react-app AppName --template typescript
            - add dependencies{ "ui": "*" }
            - change `start to dev` in package.json to run

    3. fixing ui lib to work with project
        - on (my-resume/packages/ui)
        - yarn add tsup
        - add scripts
        {
            "module": "./dist/index.mjs",
            "scripts": {
                "build": "tsup index.tsx --format esm,cjs --dts --external react",
                "dev": "tsup index.tsx --format esm,cjs --watch --dts --external react"
            },
        }

    4. Match React Version of my-resume/packages/ui and new mfe-apps

-- MicroFrontends Setup

    on( apps/mfe-apps ) ** NOTE **
    1. yarn add @craco/craco -D
    2. replace all react-scripts with craco
    3. create .cracorc.js


