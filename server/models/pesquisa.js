"use strict";

module.exports = (sequelize, DataTypes) => { 
    var Pesquisa = sequelize.define("Pesquisa", {
        dados: DataTypes.JSONB
    }, {});

    Pesquisa.associate = function(models) {
        // associations can be defined here
    };
    return Pesquisa;
};