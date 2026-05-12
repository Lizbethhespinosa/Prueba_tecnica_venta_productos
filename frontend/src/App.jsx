import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";

import CreateProduct from "./pages/CreateProduct";

import Products from "./pages/Products";


function App() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Dashboard />}
                />

                <Route
                    path="/create"
                    element={<CreateProduct />}
                />

                <Route
                    path="/products"
                    element={<Products />}
                />

            </Routes>

        </BrowserRouter>
    );
}

export default App;