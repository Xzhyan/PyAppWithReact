import { useEffect, useState } from "react";
import api from "../api";

function HomeScreen() {
  const [data, setData] = useState({});

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await api.get("/home/");
        setData(res.data);
      } catch (err) {
        console.error(err);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="w-lg bg-green-800 shadow-md rounded-b-md p-2">
      
      <p>{data.message}</p>

      <div className="w-md bg-green-950 p-2 text-black">
        <form action="" className="flex flex-col gap-2">
          <label htmlFor="username">Usuário</label>
          <input type="text" className="bg-zinc-600 p-2 outline-none shadow-md rounded-md" />

          <label htmlFor="password1">Senha</label>
          <input type="password1" className="bg-zinc-600 p-2 outline-none shadow-md rounded-md" />

          <label htmlFor="password2">Senha</label>
          <input type="password2" className="bg-zinc-600 p-2 outline-none shadow-md rounded-md" />

          <button type="submit" className="bg-green-500 p-2 w-20 rounded-md shadow-md">
            Entrar
          </button>
        </form>
      </div>
    </div>
  );
}

export default HomeScreen;
