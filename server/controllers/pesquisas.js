const Pesquisa = require('../models').Pesquisa;

module.exports = {
  create(data) {
    return Pesquisa
      .create({
        data: data.data,
        perfil: data.perfil,
	    ator: data.ator,
	    tituloNoticias: data.tituloNoticias,
	    linkNoticias: data.linkNoticias,
	    tituloResultados: data.tituloResultados,
	    linkResultados: data.linkResultados,
	    previsaoResultados: data.previsaoResultados,
	    linkPropagandas: data.linkPropagandas,
	    tituloPropagandas: data.tituloPropagandas,
	    previsaoPropagandas: data.previsaoPropagandas
      })
      .then(pesquisa => {
      	console.log('pesquisa criada: ', pesquisa)
      });
      //.then(pesquisa => res.status(201).send(pesquisa))
      //.catch(error => res.status(400).send(error));
  },
};