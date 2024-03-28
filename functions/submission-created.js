const fetch = require("node-fetch");

exports.handler = async (event) => {
  const body = JSON.parse(event.body);
  const { email, fullName, frequency } = body.payload.data;

  const response = await fetch("https://graphql.fauna.com/graphql", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.FAUNA_API_SECRET}`,
    },
    body: JSON.stringify({
      query: `
        mutation($fullName: String!, $email: String!, $frequency: String!) {
            createEntry(data: { fullName: $fullName, email: $email, frequency: $frequency } {
            _id
            fullName
            email
            frequency
          }
        }      
      `,
      variables: {
        fullName,
        frequency,
        email,
      },
    }),
  })
    .then((res) => res.json())
    .catch((err) => console.error(err));

  return {
    statusCode: 302,
    headers: {
      Location: "base.html",
      "Cache-Control": "no-cache",
    },
    body: JSON.stringify({}),
  };
};