CREATE TABLE IF NOT EXISTS Job (
    id INT,
    n_epochs INT,
    n_threads INT,
    n_islands INT,
    n_genomes INT,
    n_output_params INT,
    island_size INT,
    output_dir VARCHAR,
    exp_type VARCHAR,

    PRIMARY KEY(id, n_epochs, n_islands, n_genomes, n_output_params, island_size)
);

CREATE TABLE IF NOT EXISTS Job_InputCol (
    id INT NOT NULL,
    inputcol VARCHAR,

    PRIMARY KEY(id, inputcol),
    FOREIGN KEY(id) REFERENCES Job(id)
);
