import { useState } from "react";

import { createProduct } from "../services/productService";


function ProductForm() {

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

        } catch (error) {

            console.error(error);

            alert("Error al crear producto");
        }
    };


    return (

        <div className="glass-card">

            <h1 className="mb-4 text-dark">

                Nuevo Producto

            </h1>


            <form onSubmit={handleSubmit}>


                <div className="mb-3">

                    <label className="form-label text-dark">

                        Nombre

                    </label>

                    <input
                        type="text"
                        className="form-control"
                        placeholder="Ej. Teclado Mecánico"
                        value={nombre}
                        onChange={(e) =>
                            setNombre(e.target.value)
                        }
                        required
                    />

                </div>


                <div className="mb-3">

                    <label className="form-label text-dark">

                        Precio

                    </label>

                    <input
                        type="number"
                        className="form-control"
                        placeholder="0.00"
                        value={precio}
                        onChange={(e) =>
                            setPrecio(e.target.value)
                        }
                        required
                    />

                </div>


                <div className="mb-3">

                    <label className="form-label text-dark">

                        URL Imagen

                    </label>

                    <input
                        type="text"
                        className="form-control"
                        placeholder="https://..."
                        value={imageUrl}
                        onChange={(e) =>
                            setImageUrl(e.target.value)
                        }
                        required
                    />

                </div>


                <button
                    type="submit"
                    className="btn btn-success w-100"
                >

                    Crear Producto

                </button>

            </form>

        </div>
    );
}

export default ProductForm;