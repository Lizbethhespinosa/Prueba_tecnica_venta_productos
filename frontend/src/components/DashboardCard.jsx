function DashboardCard({
    icon,
    title,
    description,
    onClick
}) {

    return (

        <div
            className="glass-card hover-card text-center"
            onClick={onClick}
        >

            <div className="display-3 text-success mb-3">

                {icon}

            </div>

            <h3>
                {title}
            </h3>

            <p className="text-dark">

                {description}

            </p>

        </div>
    );
}

export default DashboardCard;