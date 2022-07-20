import { useEffect, useState } from "react";

export default function HttpCall() {
  const [data, setData] = useState("");

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("/get-position", {
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((responseData) => {
          console.log(responseData);
          // setData(responseData);
        });
    }, 1000);
    return () => clearInterval(interval);
  }, []);
  return (
    <>
      <h2>HTTP Communication</h2>
      <h3 className="http">{data}</h3>
    </>
  );
}
