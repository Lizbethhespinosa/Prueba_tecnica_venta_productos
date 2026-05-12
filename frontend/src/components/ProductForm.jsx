import { useState } from "react";

import { createProduct } from "../services/productService";


function ProductForm({ onProductCreated }) {

    const [nombre, setNombre] = useState("");

    const [precio, setPrecio] = useState("");

    const [imageUrl, setImageUrl] = useState("");


    const handleSubmit = async (e) => {

        e.preventDefault();

        const productData = {
            nombre: nombre,
            precio: parseFloat(precio),
            image_url: imageUrl
        };

        try {

            await createProduct(productData);

            alert("Producto creado correctamente");

            setNombre("");
            setPrecio("");
            setImageUrl("");

            onProductCreated();

        } catch (error) {

            console.error(error);

            alert("Error al crear producto");
        }
    };


    return (

        <div className="card shadow p-4">

            <h3 className="mb-4">
                Crear Producto
            </h3>

            <form onSubmit={handleSubmit}>

                <div className="mb-3">

                    <label className="form-label">
                        Nombre
                    </label>

                    <input
                        type="text"
                        className="form-control"
                        value={nombre}
                        onChange={(e) => setNombre(e.target.value)}
                        required
                    />
                </div>


                <div className="mb-3">

                    <label className="form-label">
                        Precio
                    </label>

                    <input
                        type="number"
                        className="form-control"
                        value={precio}
                        onChange={(e) => setPrecio(e.target.value)}
                        required
                    />
                </div>


                <div className="mb-3">

                    <label className="form-label">
                        URL Imagen
                    </label>

                    <input
                        type="text"
                        className="form-control"
                        value={imageUrl}
                        onChange={(e) => setImageUrl(e.target.value)}
                        required
                    />
                </div>


                <button
                    type="submit"
                    className="btn btn-primary w-100"
                >
                    Guardar Producto
                </button>

            </form>

        </div>
    );
}

export default ProductForm;