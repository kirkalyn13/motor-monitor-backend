# Motor Monitor Backend

Backend for the Induction Motor Monitoring System. 

To view sensor readings and analysis, visit the [web app](https://motor-monitor-frontend.vercel.app/).

## Tech Stack
- **Flask** - Framework
- **PostgreSQL** - Database
- **Gunicorn** - WSGI HTTP Server
- **Render** - For deployment


## Installation

1. Clone repository
2. Run `pip install -r requirements.txt`
3. Run `python main.py`

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_HOST`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DB_PORT`


## Deployment
Merging to main automatically deploys to [Render](https://dashboard.render.com/).

To view production frontend website, visit [here](https://motor-monitor-frontend.vercel.app/).


## Authors

- [Engr. Kirk Alyn Santos](https://github.com/kirkalyn13)

## License

[MIT](https://choosealicense.com/licenses/mit/)
