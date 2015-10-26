Stats API


JSON Format

[
  {
    user: {
      username: string,
      password?: <password>

      activities: {
        title: string
        units: string (miles, km, flights, etc.)
        stats: [
          {
            date: DateTime
            number_of: integer

          },
        ]
    }
]
