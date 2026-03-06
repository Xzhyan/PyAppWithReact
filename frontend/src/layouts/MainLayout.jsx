import { Outlet } from "react-router-dom";

function MainLayout() {
  return (
    <>
      <header className="w-full p-2 bg-green-950 shadow-md">
        <h1 className="font-semibold">Python App with React</h1>
      </header>

      <main className="flex justify-center">
        <Outlet />
      </main>
    </>
  );
}

export default MainLayout;
