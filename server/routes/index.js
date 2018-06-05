const pesquisasController = require('../controllers').pesquisas;

module.exports = (app) => {
  app.get('/api', (req, res) => res.status(200).send({
    message: 'Bem vindo à API do observatório.',
  }));

  app.post('/api/pesquisas', pesquisasController.create);
  app.get('/api/pesquisas', pesquisasController.list);
  app.get('/api/pesquisas/:pesquisaId', pesquisasController.retrieve);
  app.get('/api/pesquisas/perfil/:perfil', pesquisasController.listByPerfil);
  app.get('/api/pesquisas/ator/:ator', pesquisasController.listByAtor);
  app.get('/api/pesquisas/data/:data', pesquisasController.listByData);
  app.get('/api/datas', pesquisasController.listDatas);
  app.get('/api/atores', pesquisasController.listAtores);
};