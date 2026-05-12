function ProductCard({ product }) {

    return (

        <div className="card shadow h-100 rounded-4">

            <img
                src={product.image_url}
                className="card-img-top"
                alt={product.nombre}
                style={{
                    height: "220px",
                    objectFit: "cover"
                }}
            />

            <div className="card-body">
                <div className="divNombreProducto">
                <h5>
                    Nombre del producto:
                </h5>
                <h4>
                    {product.nombre}
                </h4>
                </div>
                <div className="divPrecioProducto">
                <h5>
                    Precio del producto:
                </h5>
                <h4 className="text-success">

                    ${product.precio}

                </h4>
                </div>

            </div>

        </div>
    );
}

export default ProductCard;