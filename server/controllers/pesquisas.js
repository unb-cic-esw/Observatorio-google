const Pesquisa = require('../models').Pesquisa;

module.exports = {
    create(req, res) {
        let data = req.body;
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
            .then(pesquisa => res.status(201).send(pesquisa))
            .catch(error => res.status(400).send(error));
    },

    createLocal(data) {
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
            });
    },

    list(req, res) {
        return Pesquisa
            .all()
            .then(pesquisas => res.status(200).send(pesquisas))
            .catch(error => res.status(400).send(error));
    },

    retrieve(req, res) {
            return Pesquisa
                .findById(req.params.pesquisaId)
                .then(pesquisa => {
                    if (!pesquisa) {
                        return res.status(404).send({
                            message: 'pesquisa não encontrada',
                        });
                    }
                    return res.status(200).send(pesquisa);
                })
                .catch(error => res.status(400).send(error));
    },

    listByPerfil(req,res) {
        return Pesquisa
            .findAll({
                where: {
                    perfil: req.params.perfil
                }
            })
            .then(pesquisas => res.status(200).send(pesquisas))
            .catch(error => res.status(400).send(error));
    },

    listByAtor(req,res) {
        return Pesquisa
            .findAll({
                where: {
                    ator: req.params.ator
                }
            })
            .then(pesquisas => res.status(200).send(pesquisas))
            .catch(error => res.status(400).send(error));
    },

    listByData(req,res) {
        return Pesquisa
            .findAll({
                where: {
                    data: req.params.data
                }
            })
            .then(pesquisas => res.status(200).send(pesquisas))
            .catch(error => res.status(400).send(error));
    }
};