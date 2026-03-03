import { useEffect, useState } from "react";
import api from "../api";

function HomeScreen() {
  const [data, setData] = useState({});

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await api.get("/api/");
        setData(res.data);
      } catch (err) {
        console.error(err);
      }
    }

    fetchData();
  }, []);

  return (
    <div>
      <p>Conteudo do home</p>
      <p>{data.message}</p>
    </div>
  );
}

export default HomeScreen;
