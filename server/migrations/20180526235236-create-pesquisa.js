'use strict';
module.exports = {
  up: (queryInterface, Sequelize) => {
    return queryInterface.createTable('Pesquisas', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      data: {
        type: Sequelize.STRING
      },
      perfil: {
        type: Sequelize.STRING
      },
      ator: {
        type: Sequelize.STRING
      },
      tituloNoticias: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      linkNoticias: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      tituloResultados: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      linkResultados: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      previsaoResultados: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      linkPropagandas: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      tituloPropagandas: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      previsaoPropagandas: {
        type: Sequelize.ARRAY(Sequelize.STRING)
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: (queryInterface, Sequelize) => {
    return queryInterface.dropTable('Pesquisas');
  }
};