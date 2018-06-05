const Pesquisa = require('../models').Pesquisa;
let Sequelize = require('sequelize');

module.exports = {
    create(req, res) {
        let data = req.body;
        return Pesquisa
            .create({
                dados: data
            })
            .then(pesquisa => res.status(201).send(pesquisa))
            .catch(error => res.status(400).send(error));
    },

    createLocal(data) {
        return Pesquisa
            .create({
                dados: data
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
                    dados:{
                        perfil: req.params.perfil
                    }
                }
            })
            .then(pesquisas => res.status(200).send(pesquisas))
            .catch(error => res.status(400).send(error));
    },

    listByAtor(req,res) {
        return Pesquisa
            .findAll({
                where: {
                    dados:{
                        ator: req.params.ator
                    }
                }
            })
            .then(pesquisas => res.status(200).send(pesquisas))
            .catch(error => res.status(400).send(error));
    },

    listByData(req,res) {
        return Pesquisa
            .findAll({
                where: {
                    dados:{
                        data: req.params.data
                    }
                }
            })
            .then(pesquisas => res.status(200).send(pesquisas))
            .catch(error => res.status(400).send(error));
    },

    listDatas(req,res) {
        return Pesquisa
            .findAll({
                attributes: [[Sequelize.json('dados.data'),'data']],
                group: [[[Sequelize.json('dados.data')]]]
            })
            .then(pesquisas => res.status(200).send(pesquisas))
            .catch(error => res.status(400).send(error));
    },

    listAtores(req,res) {
        return Pesquisa
            .findAll({
                attributes: [[Sequelize.json('dados.ator'),'ator']],
                group: [[[Sequelize.json('dados.ator')]]]
            })
            .then(pesquisas => res.status(200).send(pesquisas))
            .catch(error => res.status(400).send(error));
    }
};