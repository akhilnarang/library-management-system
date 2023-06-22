# library-management-system

## Setup and running
- Install [rye](https://rye-up.com/guide/installation/)
- Run `rye sync` to install dependencies
- Populate your `.env` file with the required variables if they aren't in your environment already
  - `DB_NAME` - The name of the database to use
  - `DB_USER` - The username to use when connecting to the database
  - `DB_HOST` - The host to connect to
  - `DB_PASSWORD` - The password to use when connecting to the database
  - `DB_SSLMODE` - The SSL mode to use when connecting to the database. Defaults to `disable
  - `DB_PORT` - The port to connect to. Defaults to `5432`
  - `DB_URI` - alternatively, you can just use a postgres database URI to connect to the database
  - `MOCK_FRAPPE_CLIENT` - This can be used if Frappe's book API is down, set it to true to use a mock client instead
- Run database migrations by running `rye run migrate`
- Start the server by running `rye run devserver`

## Screenshots
- They can be found [here](/screenshots.md)
