from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from decimal import Decimal
from flask_cors import CORS
from bson import ObjectId


from flask_marshmallow import Marshmallow
from datetime import datetime

from dotenv import load_dotenv
from pathlib import Path
import os

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


basepath = Path()
basedir = str(basepath.cwd())
env_path = basepath.cwd() / '.env'
load_dotenv(env_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=str(os.getenv("DATABASE_URI"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

CORS(app)

db = SQLAlchemy(app)
metadata = MetaData()
Base = declarative_base()
ma = Marshmallow(app)

class User(object):
    def __init__(self, id, username, password, codvendedor):
        self.id = id
        self.username = username
        self.password = password
        self.codVendedor = codvendedor

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'jbello', 'euro2010', '01'),
    User(2, 'jroquez', 'jr123456', '02'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)



jwt = JWT(app, authenticate, identity)





class SAFACT(Base, db.Model):
    __table__ = db.Table('SAFACT', metadata, 
                         db.Column('NroUnico', db.Integer, primary_key=True, autoincrement=True), 
                         implicit_returning=False,
                         autoload=True, autoload_with=db.engine)
    def __init__(self, NumeroD,Cambio,CancelA,CancelC,CancelE,CancelG,CancelI,CancelP,CancelT,Contado,CostoPrd,CostoSrv,Descto1,Descto2,DesctoP,
                 MontoMEx,MtoComiCob,MtoComiCobD,MtoComiVta,MtoComiVtaD,MtoExtra,MtoFinanc,MtoInt1,MtoInt2,MtoNCredito,MtoNDebito,MtoPagos,
                 MtoTax,PctAnual,PctManejo,RetenIVA,SaldoAct,TGravable,TGravable0,TotalSrv,ValorPtos,Fletes,EsCorrel,FromTran,
                 EstadoFE,NGiros,NMeses,TipoTraE,TipoFac,Factor,Signo,FechaE,FechaI,FechaT,FechaV,Credito,Monto,MtoTotal,TExento,TotalPrd,
                 CodClie,CodEsta,CodSucu,CodUbic,CodUsua,CodVend,Descrip,Direc1,ID3):
        self.NumeroD = NumeroD
        self.Cambio = Cambio
        self.CancelA = CancelA
        self.CancelC = CancelC
        self.CancelE = CancelE
        self.CancelG = CancelG
        self.CancelI = CancelI
        self.CancelP = CancelP
        self.CancelT = CancelT
        self.Contado = Contado
        self.CostoPrd = CostoPrd
        self.CostoSrv = CostoSrv
        self.Descto1 = Descto1
        self.Descto2 = Descto2
        self.DesctoP = DesctoP
        self.MontoMEx = MontoMEx
        self.MtoComiCob = MtoComiCob
        self.MtoComiCobD = MtoComiCobD
        self.MtoComiVta = MtoComiVta
        self.MtoComiVtaD = MtoComiVtaD
        self.MtoExtra = MtoExtra
        self.MtoFinanc = MtoFinanc
        self.MtoInt1 = MtoInt1
        self.MtoInt2 = MtoInt2
        self.MtoNCredito = MtoNCredito
        self.MtoNDebito = MtoNDebito
        self.MtoPagos = MtoPagos
        self.MtoTax = MtoTax
        self.PctAnual = PctAnual
        self.PctManejo = PctManejo
        self.RetenIVA = RetenIVA
        self.SaldoAct = SaldoAct
        self.TGravable = TGravable
        self.TGravable0 = TGravable0
        self.TotalSrv = TotalSrv
        self.ValorPtos = ValorPtos
        self.Fletes = Fletes
        self.EsCorrel = EsCorrel
        self.FromTran = FromTran
        self.EstadoFE = EstadoFE
        self.NGiros = NGiros
        self.NMeses = NMeses
        self.TipoTraE = TipoTraE
        self.TipoFac = TipoFac
        self.Factor = Factor
        self.Signo = Signo
        self.FechaE = FechaE
        self.FechaI = FechaI
        self.FechaT = FechaT
        self.FechaV = FechaV
        self.Credito = Credito
        self.Monto = Monto
        self.MtoTotal = MtoTotal
        self.TExento = TExento
        self.TotalPrd = TotalPrd
        self.CodClie = CodClie
        self.CodEsta = CodEsta
        self.CodSucu = CodSucu
        self.CodUbic = CodUbic
        self.CodUsua = CodUsua
        self.CodVend = CodVend
        self.Descrip = Descrip
        self.Direc1 = Direc1
        self.ID3 = ID3 

class SAITEMFAC(Base, db.Model):
    __table__ = db.Table('SAITEMFAC', metadata, autoload=True, autoload_with=db.engine)
    def __init__(self,CantidadA,CantidadD,CantidadO,CantidadT,CantidadU,CantidadUA,MtoTax,MtoTaxO,ExistAntU,Descto,Tara,DEsComp,DEsLote,DEsSeri,EsExento,
                 EsFreeP,EsPesa,EsServ,EsUnid,Signo,CodSucu,CantMayor,FechaE,FechaL,FechaV,TipoFac,TipoPVP,Factor,NroLineaC,NroUnicoL,ONroLinea,
                 ONroLineaC,Refere,UsaServ,Cantidad,CodItem,CodUbic,CodVend,Costo,Descrip1,ExistAnt,NroLinea,NumeroD,Precio,PriceO,TotalItem):
        self.CantidadA = CantidadA
        self.CantidadD = CantidadD
        self.CantidadO = CantidadO
        self.CantidadT = CantidadT
        self.CantidadU = CantidadU
        self.CantidadUA = CantidadUA 
        self.MtoTax = MtoTax
        self.MtoTaxO = MtoTaxO
        self.ExistAntU = ExistAntU
        self.Descto = Descto
        self.Tara = Tara
        self.DEsComp = DEsComp
        self.DEsLote = DEsLote
        self.DEsSeri = DEsSeri
        self.EsExento = EsExento
        self.EsFreeP = EsFreeP
        self.EsPesa = EsPesa 
        self.EsServ = EsServ
        self.EsUnid = EsUnid
        self.Signo = Signo 
        self.CodSucu = CodSucu
        self.CantMayor = CantMayor
        self.FechaE = FechaE
        self.FechaL = FechaL
        self.FechaV = FechaV
        self.TipoFac = TipoFac
        self.TipoPVP = TipoPVP
        self.Factor = Factor
        self.NroLineaC = NroLineaC
        self.NroUnicoL = NroUnicoL
        self.ONroLinea =  ONroLinea
        self.ONroLineaC = ONroLineaC
        self.Refere = Refere
        self.UsaServ = UsaServ
        self.Cantidad = Cantidad
        self.CodItem = CodItem
        self.CodUbic = CodUbic
        self.CodVend = CodVend
        self.Costo = Costo
        self.Descrip1 = Descrip1
        self.ExistAnt = ExistAnt
        self.NroLinea = NroLinea
        self.NumeroD = NumeroD
        self.Precio = Precio
        self.PriceO = PriceO
        self.TotalItem = TotalItem

class SACORRELSIS(Base, db.Model):
    __table__ = db.Table('SACORRELSIS', metadata, autoload=True, autoload_with=db.engine)
    def __init__(self, ValueInt, PrxPedido):
        self.ValueInt = ValueInt
        self.PrxPedido = PrxPedido

class SAEXIS(db.Model):
    CodProd = db.Column(db.VARCHAR(length=15), primary_key=True, nullable=False)
    CodUbic = db.Column(db.VARCHAR(length=10), primary_key=True, nullable=False)
    PuestoI = db.Column(db.VARCHAR(length=10))
    Existen = db.Column(db.DECIMAL(precision=28, scale=4))
    ExUnidad = db.Column(db.DECIMAL(precision=28, scale=4))
    CantPed = db.Column(db.DECIMAL(precision=28, scale=4))
    UnidPed = db.Column(db.DECIMAL(precision=28, scale=4))
    CantCom = db.Column(db.DECIMAL(precision=28, scale=4))
    UnidCom = db.Column(db.DECIMAL(precision=28, scale=4))

    def __init__(self, CodProd, CodUbic, Puestol, Existen, ExUnidad, CantPed, UniPed, CantCom, UnidCom):
        self.CodProd = CodProd
        self.CodUbic = CodUbic
        self.PuestoI = PuestoI
        self.Existen = Existen
        self.ExUnidad = ExUnidad
        self.CantPed = CantPed
        self.UnidPed = UnidPed
        self.CantCom = CantCom
        self.UnidCom = UnidCom

class ExisSchema(ma.Schema):
    class Meta:
        fields=('CodProd','CodUbic','PuestoI','Existen','ExUnidad','CantPed','UnidPed','CantCom','UnidCom')
exis_schema= ExisSchema()
exiss_schema= ExisSchema(many=True)

class SAPROD(Base, db.Model):
    __table__ = db.Table('SAPROD', metadata, autoload=True, autoload_with=db.engine)
    def __init__(self, CodProd, Descrip, Precio1,CostAct,Existen,Compro):
        self.CodProd = CodProd
        self.Descrip = Descrip
        self.Precio1 = Precio1
        self.CostAct = CostAct
        self.Existen = Existen
        self.Compro = Compro

class ProdSchema(ma.Schema):
    class Meta:
        fields=('CodProd', 'Descrip', 'Precio1','CostAct','Existen','Compro')
prod_schema= ProdSchema()
prods_schema= ProdSchema(many=True)

class SACLIE(Base, db.Model):
    __table__ = db.Table('SACLIE', metadata, autoload=True, autoload_with=db.engine)
    def __init__(self, CodClie, Descrip, CodVend, Saldo, Direc1):
        self.CodClie = CodClie
        self.Descrip = Descrip
        self.CodVend = CodVend
        self.Saldo = Saldo
        self.Direc1 = Direc1
        

@app.route('/protectec')
@jwt_required()
def protected():
    userdata= {
        "userVend":current_identity.username,
        "CodVend": current_identity.codVendedor
    }
   
    return jsonify(userdata)



@app.route('/', methods=['GET'])
def index():
    Hola="Hola"
    return jsonify(Hola)
        
@app.route('/send', methods=['POST'])
def send_pedido():
    try:
        orders = request.json['order']
        correlsis = SACORRELSIS.query.filter_by(FieldName='PrxPedido')
        for row in correlsis:
            correl = int(row.ValueInt)
        for order in orders:
            NumeroD =  correl
            Cambio  = 0.0000
            CancelA = 0.0000
            CancelC = 0.0000
            CancelE = 0.0000
            CancelG = 0.0000
            CancelI = 0.0000
            CancelP = 0.0000
            CancelT = 0.0000
            Contado = 0.0000
            CostoPrd = 0.0000
            CostoSrv = 0.0000
            Descto1 = 0.0000
            Descto2 = 0.0000
            DesctoP = 0.0000
            MontoMEx = 0.0000
            MtoComiCob = 0.0000
            MtoComiCobD = 0.0000
            MtoComiVta = 0.0000
            MtoComiVtaD = 0.0000
            MtoExtra = 0.0000
            MtoFinanc = 0.0000
            MtoInt1 = 0.0000
            MtoInt2 = 0.0000
            MtoNCredito = 0.0000
            MtoNDebito = 0.0000
            MtoPagos = 0.0000
            MtoTax = 0.0000
            PctAnual = 0.0000
            PctManejo = 0.0000
            RetenIVA = 0.0000
            SaldoAct = 0.0000
            TGravable = 0.0000
            TGravable0 = 0.0000
            TotalSrv = 0.0000
            ValorPtos = 0.0000
            Fletes = 0.0000
            """ SMALL VALUE """
            EsCorrel = 1
            FromTran = 0
            EstadoFE = 0
            NGiros = 0
            NMeses = 0
            TipoTraE = 0
            TipoFac = "E"
            Factor = 1.0000
            Signo = 1
            """ Fechas """
            FechaE = datetime.now()
            FechaI = datetime.now()
            FechaT = datetime.now()
            FechaV = datetime.now()

            """ Totales """
            Credito = order['MtoTotal']
            Monto = order['MtoTotal']
            MtoTotal = order['MtoTotal']
            TExento = order['MtoTotal']
            TotalPrd = order['MtoTotal']
            """ Resquest JSON """
            CodClie = order['CodClie']
            CodEsta = "EGPLCTS01"
            CodSucu = "00000"
            CodUbic = "01"
            CodUsua = "001"
            CodVend = order['CodVend']
            Descrip = order['Descrip']
            Direc1  = order['Direc1']
            ID3 = order['CodClie']
    
            new_order = SAFACT(NumeroD,Cambio,CancelA,CancelC,CancelE,CancelG,CancelI,CancelP,CancelT,Contado,CostoPrd,CostoSrv,Descto1,Descto2,DesctoP,
                           MontoMEx,MtoComiCob,MtoComiCobD,MtoComiVta,MtoComiVtaD,MtoExtra,MtoFinanc,MtoInt1,MtoInt2,MtoNCredito,MtoNDebito,MtoPagos,
                           MtoTax,PctAnual,PctManejo,RetenIVA,SaldoAct,TGravable,TGravable0,TotalSrv,ValorPtos,Fletes,EsCorrel,FromTran,
                           EstadoFE,NGiros,NMeses,TipoTraE,TipoFac,Factor,Signo,FechaE,FechaI,FechaT,FechaV,Credito,Monto,MtoTotal,TExento,TotalPrd,
                           CodClie,CodEsta,CodSucu,CodUbic,CodUsua,CodVend,Descrip,Direc1,ID3)
                                   
            db.session.add(new_order)
            for item in order['items']:
                CantidadA = 0.0000
                CantidadD = 0.0000
                CantidadO = 0.0000
                CantidadT = 0.0000
                CantidadU = 0.0000
                CantidadUA = 0.0000
                MtoTax = 0.0000
                MtoTaxO = 0.0000
                ExistAntU = 0.0000
                Descto = 0.0000
                Tara = 0.0000
                DEsComp = 0
                DEsLote = 0
                DEsSeri = 0
                EsExento = 1
                EsFreeP = 0
                EsPesa = 0
                EsServ = 0
                EsUnid = 0
                Signo = 1
                CodSucu = "00000"
                CantMayor = 1.0000
                """ Fecha """
                FechaE = datetime.now()
                FechaL = datetime.now()
                FechaV = datetime.now()
                """ Revisar """
                TipoFac = "E"
                TipoPVP = 3
                Factor = 1.0000
                NroLineaC = 0
                NroUnicoL = 0
                ONroLinea = 0
                ONroLineaC = 0
                Refere = "01"
                UsaServ = 0
                """ Request JSON """
                Cantidad = item.get('Cantidad')
                CodItem = item.get('CodItem')
                CodUbic = "01"
                CodVend = item.get('CodVend')
                Costo = item.get('Costo')
                Descrip1 = item.get('Descrip1')
                ExistAnt = item.get('ExistAnt')
                NroLinea = item.get('NroLinea')
                NumeroD = correl
                Precio = item.get('Precio')
                PriceO = item.get('Precio')
                TotalItem = item.get('TotalItem')
                new_itemorder = SAITEMFAC(CantidadA,CantidadD,CantidadO,CantidadT,CantidadU,CantidadUA,MtoTax,MtoTaxO,ExistAntU,Descto,Tara,DEsComp,DEsLote,DEsSeri,EsExento,
                                       EsFreeP,EsPesa,EsServ,EsUnid,Signo,CodSucu,CantMayor,FechaE,FechaL,FechaV,TipoFac,TipoPVP,Factor,NroLineaC,NroUnicoL,ONroLinea,
                                       ONroLineaC,Refere,UsaServ,Cantidad,CodItem,CodUbic,CodVend,Costo,Descrip1,ExistAnt,NroLinea,NumeroD,Precio,PriceO,TotalItem)
                db.session.add(new_itemorder)
                saitem =  db.session.query(SAEXIS).filter_by(CodProd=int(item.get('CodItem')))
                """ for row in saitem:
                    if int(row.Existen) < (int(row.CantCom) + int(Cantidad)):
                        Disp=int(row.Existen)-int(row.CantCom)
                        raise ValueError('SKU:', row.CodProd, 'Disponibilidad:',Disp,'Pedido:', item.get('Cantidad')) """

                result = exiss_schema.dump(saitem)
                for i in result:
                    if int(i['Existen']) < int(i['CantCom'] + int(Cantidad)):
                        Disp=int(i['Existen'])-int(i['CantCom'])
                        raise ValueError('SKU:',i['CodProd'], 'Disponibilidad:',Disp,'Pedido:',item.get('Cantidad')) 

                
                
                db.session.query(SAEXIS).filter_by(CodProd=item.get('CodItem')).update({'CantCom': SAEXIS.CantCom + Cantidad})
                db.session.query(SAPROD).filter_by(CodProd=item.get('CodItem')).update({'Compro': SAPROD.Compro + Cantidad})
        prox =correl + 1
        db.session.query(SACORRELSIS).filter_by(FieldName='PrxPedido').update({'ValueInt': prox})
        db.session.commit()
        return  jsonify(message = "Pedido enviado Exitosamente")
    except Exception as e: 
        return str(e)

@app.route('/skus', methods=['GET'])
def get_productos():
    prod = []
    all_prod = SAPROD.query.filter(SAPROD.Existen > SAPROD.Compro)
    
    for row in all_prod:
        prod.append({
            'CodProd': str(row.CodProd),
            'Descrip': str(row.Descrip),
            'Precio1': str(float(row.Precio1)),
            'CostAct': str(float(row.CostAct)),
            'Existen': str(int(row.Existen)-int(row.Compro))
        })
    return jsonify(prod)

@app.route('/clientes/<id>', methods=['GET'])
def get_clientes(id):
    clientes = []
    all_clientes = SACLIE.query.filter_by(CodVend=id)
   
    for row in all_clientes:
        clientes.append({
            'codigo': str(row.CodClie),
            'nombre': str(row.Descrip),
            'vendedor': str(row.CodVend),
            'saldo': str(float(row.Saldo)),
            'Direc1': str(row.Direc1)

        })


    return jsonify(clientes)

@app.route('/pedidos/<id>', methods=['GET'])
def get_pedidos(id):
    pedidos = []
    all_pedidos = SAFACT.query.filter_by(CodVend=id)
    
    for row in all_pedidos:
        pedidos.append({
            'NumeroD': str(row.NumeroD),
            'Descrip': str(row.Descrip),
            'MtoTotal': str(float(row.MtoTotal)),
            'FechaE': str((row.FechaE).strftime("%W-%m-%Y"))

        })


    return jsonify(pedidos)





if __name__ == "__main__":
    app.run(debug=True)