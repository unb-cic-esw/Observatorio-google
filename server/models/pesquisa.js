'use strict';
module.exports = (sequelize, DataTypes) => {
  var Pesquisa = sequelize.define('Pesquisa', {
    data: DataTypes.STRING,
    perfil: DataTypes.STRING,
    ator: DataTypes.STRING,
    tituloNoticias: DataTypes.ARRAY(DataTypes.STRING),
    linkNoticias: DataTypes.ARRAY(DataTypes.STRING),
    tituloResultados: DataTypes.ARRAY(DataTypes.STRING),
    linkResultados: DataTypes.ARRAY(DataTypes.STRING),
    previsaoResultados: DataTypes.ARRAY(DataTypes.STRING),
    linkPropagandas: DataTypes.ARRAY(DataTypes.STRING),
    tituloPropagandas: DataTypes.ARRAY(DataTypes.STRING),
    previsaoPropagandas: DataTypes.ARRAY(DataTypes.STRING)
  }, {});
  Pesquisa.associate = function(models) {
    // associations can be defined here
  };
  return Pesquisa;
};