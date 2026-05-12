function ProductCard({ product }) {

    return (

        <div className="card shadow h-100">

            <img
                src={product.image_url}
                className="card-img-top"
                alt={product.nombre}
                style={{
                    height: "250px",
                    objectFit: "cover"
                }}
            />

            <div className="card-body">

                <h5 className="card-title">
                    {product.nombre}
                </h5>

                <p className="card-text">

                    <strong>
                        Precio:
                    </strong>

                    {" "}
                    ${product.precio}

                </p>

            </div>

        </div>
    );
}

export default ProductCard;