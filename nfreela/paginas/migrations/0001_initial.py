# Generated by Django 3.1.6 on 2022-04-30 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=30, verbose_name='Nome da Empresa:')),
                ('nome_fantasia', models.CharField(max_length=30, verbose_name='Nome fantasia:')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ:')),
                ('cidade_empresa', models.CharField(choices=[('Acari', 'Acari'), ('Afonso Bezerra', 'Afonso Bezerra'), ('Agua Nova', 'Água Nova'), ('Alexandria', 'Alexandria'), ('Almino Afonso', 'Almino'), ('Alto do Rodrigues', 'Alto do Rodrigues'), ('Angicos', 'Angicos'), ('Antônio Martins', 'Antônio Martins'), ('Apodi', 'Apodi'), ('Areia Branca', 'Areia Branca'), ('Arez', 'Arez'), ('Assu', 'Assu'), ('Baia Formosa', 'Baía Formosa'), ('Baraúna', 'Baraúna'), ('Barcelona', 'Barcelona'), ('Bento Fernandes', 'Bento Fernandes'), ('Boa Saúde', 'Boa Saúde'), ('Bodó', 'Bodó'), ('Bom Jesus', 'Bom Jesus'), ('Brejinho', 'Brejinho'), ('Caicara do Norte', 'Caiçara do Norte'), ('Caicara do Rio do Vento', 'Caiçara do Rio do Vento'), ('Caicó', 'Caicó'), ('Campo Grande', 'Campo Grande'), ('Campo Redondo', 'Campo Redondo'), ('Canguaretama', 'Canguaretama'), ('Caraúbas', 'Caraúbas'), ('Carnauba dos Dantas', 'Carnaúba dos Dantas'), ('Carnaubais', 'Carnaubais'), ('Ceará Mirim', 'Ceará-Mirim'), ('Cerro corá', 'Cerro Corá'), ('Coronel Ezequiel', 'Coronel Ezequiel'), ('Coronel João Pessoa', 'Coronel João Pessoa'), ('cruzeta', 'Cruzeta'), ('Currais Novos', 'Currais Novos'), ('Doutor Severiano', 'Doutor Severiano'), ('Encanto', 'Encanto'), ('Equador', 'Equador'), ('Espirito Santo', 'Espírito Santo'), ('Extremoz', 'Extremoz'), ('Felipe Guerra', 'Felipe Guerra'), ('Fernando Pedroza', 'Fernando Pedroza'), ('Florãnia', 'Florânia'), ('Francisco Dantas', 'Francisco Dantas'), ('Frutuoso Gomes', 'Frutuoso Gomes'), ('Galinhos', 'Galinhos'), ('Goianinha', 'Goianinha'), ('Governador Dix-sept Rosado', 'Governador Dix-Sept Rosado'), ('Grossos', 'Grossos'), ('Guamaré', 'Guamaré'), ('Ielmo Marinho', 'Ielmo Marinho'), ('Ipanguaçu', 'Ipanguaçu'), ('Ipueira', 'Ipueira'), ('Itajá', 'Itajá'), ('Itaú', 'Itaú'), ('Jaçanã', 'Jaçanã'), ('Jandaíra', 'Jandaíra'), ('Janduís', 'Janduís'), ('Japi', 'Japi'), ('Jardim de Angicos', 'Jardim de Angicos'), ('Jardim de Piranhas', 'Jardim de Piranhas'), ('Jardim do seridó', 'Jardim do Seridó'), ('João Cãmara', 'João Câmara'), ('João Dias', 'João Dias'), ('José da Penha', 'José da Penha'), ('Jucurutu', 'Jucurutu'), ('Jundiá', 'Jundiá'), ('Lagoa d´Anta', 'Lagoa dAnta'), ('Lagoa de Pedras', 'Lagoa de Pedras'), ('Lagoa de Velhos', 'Lagoa de Velhos'), ('Lagoa Nova', 'Lagoa Nova'), ('Lagoa Salgada', 'Lagoa Salgada'), ('Lajes', 'Lajes'), ('Lajes Pintadas', 'Lajes Pintadas'), ('Lucrécia', 'Lucrécia'), ('Luis Gomes', 'Luís Gomes'), ('Macaiba', 'Macaíba'), ('Macau', 'Macau'), ('Major Sales', 'Major Sales'), ('Marcelino Vieira', 'Marcelino Vieira'), ('Martins', 'Martins'), ('Maxaranguape', 'Maxaranguape'), ('Messias Targino', 'Messias Targino'), ('Montanhas', 'Montanhas'), ('Monte Alegre', 'Monte Alegre'), ('Monte das Gameleiras', 'Monte das Gameleiras'), ('Mossoró', 'Mossoró'), ('Natal', 'Natal'), ('Nisia Floresta', 'Nísia Floresta'), ('Nova Cruz', 'Nova Cruz'), ('Olho d´Água doS Borges', 'Olho-dÁgua do Borges'), ('Parana', 'Paraná'), ('Parau', 'Paraú'), ('Parazinho', 'Parazinho'), ('Parelhas', 'Parelhas'), ('Parnamirim', 'Parnamirim'), ('Passa e Fica', 'Passa-e-Fica'), ('Passagem', 'Passagem'), ('Patu', 'Patu'), ('Pau dos Ferros', 'Pau dos Ferros'), ('Pedra Grande', 'Pedra Grande'), ('Pedra Preta', 'Pedra Preta'), ('Pedro Avelino', 'Pedro Avelino'), ('Pedro Velho', 'Pedro Velho'), ('Pendências', 'Pendências'), ('Pilões', 'Pilões'), ('Poço Branco', 'Poço Branco'), ('Portalegre', 'Portalegre'), ('Porto do Mangue', 'Porto do Mangue'), ('Pureza', 'Pureza'), ('Rafael Fernandes', 'Rafael Fernandes'), ('Rafael Godeiro', 'Rafael Godeiro'), ('Riacho da Cruz', 'Riacho da Cruz'), ('Riacho de Santana', 'Riacho de Santana'), ('Riachuelo', 'Riachuelo'), ('Rio do Fogo', 'Rio do Fogo'), ('Rodolfo Fernandes', 'Rodolfo Fernandes'), ('Santa Cruz', 'Santa Cruz'), ('Santa Maria', 'Santa Maria'), ('Santana do Matos', 'Santana do Matos'), ('Santana do Seridó', 'Santana do Seridó'), ('Santo Antônio', 'Santo Antônio'), ('São Bento do Norte', 'São Bento do Norte'), ('São Bento do Trairi', 'São Bento do Trairi'), ('São Fernando', 'São Fernando'), ('São Francisco do Oeste', 'São Francisco do Oeste'), ('São Gonçalo do Amarante', 'São Gonçalo do Amarante'), ('São João do Sabugi', 'São João do Sabugi'), ('São José de Mipibu', 'São José de Mipibu'), ('São José do Campestre', 'São José do Campestre'), ('São José do Seridó', 'São José do Seridó'), ('São Miguel', 'São Miguel'), ('São Miguel do Gostoso', 'São Miguel do Gostoso'), ('São Paulo do Potengi', 'São Paulo do Potengi'), ('São Pedro', 'São Pedro'), ('São Rafael', 'São Rafael'), ('São Tomé', 'São Tomé'), ('Senador Elói de Souza', 'Senador Elói de Souza'), ('senadorgeorginoavelino', 'Senador Georgino Avelino'), ('Serra Caiada', 'Serra Caiada'), ('Serra de São Bento', 'Serra de São Bento'), ('Serra do Mel', 'Serra do Mel'), ('Serra Negra do Norte', 'Serra Negra do Norte'), ('Serrinha', 'Serrinha'), ('Serrinha dos Pintos', 'Serrinha dos Pintos'), ('Severiano Melo', 'Severiano Melo'), ('Sitio Novo', 'Sítio Novo'), ('Taboleiro Grande', 'Taboleiro Grande'), ('Taipu', 'Taipu'), ('Tangará', 'Tangará'), ('Tenente Ananias', 'Tenente Ananias'), ('Tenentel Laurentino Cruz', 'Tenente Laurentino Cruz'), ('Tibau', 'Tibau'), ('Tibau do Sul', 'Tibau do Sul'), ('Timbaúba dos Batistas', 'Timbaúba dos Batistas'), ('Touros', 'Touros'), ('Triunfo Potiguar', 'Triunfo Potiguar'), ('Umarizal', 'Umarizal'), ('Upanema', 'Upanema'), ('Várzea', 'Várzea'), ('Venha-ver', 'Venha-Ver'), ('Vera Cruz', 'Vera Cruz'), ('Viçosa', 'Viçosa'), ('Vila Flor', 'Vila Flor')], max_length=30, verbose_name='Cidade:')),
                ('telefone_empresa', models.CharField(max_length=11, verbose_name='Telefone:')),
                ('email_empresa', models.EmailField(max_length=254, verbose_name='Email:')),
                ('rua_empresa', models.CharField(max_length=100, verbose_name='Rua:')),
                ('bairro_empresa', models.CharField(max_length=100, verbose_name='Bairro:')),
                ('ramo_empresa', models.CharField(max_length=50, verbose_name='Ramo:')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('mudando', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Processos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_vaga', models.CharField(max_length=30, verbose_name='Nome da Empresa:')),
                ('vaga', models.CharField(max_length=30, verbose_name='Vaga:')),
                ('cidade_vaga', models.CharField(choices=[('Acari', 'Acari'), ('Afonso Bezerra', 'Afonso Bezerra'), ('Agua Nova', 'Água Nova'), ('Alexandria', 'Alexandria'), ('Almino Afonso', 'Almino'), ('Alto do Rodrigues', 'Alto do Rodrigues'), ('Angicos', 'Angicos'), ('Antônio Martins', 'Antônio Martins'), ('Apodi', 'Apodi'), ('Areia Branca', 'Areia Branca'), ('Arez', 'Arez'), ('Assu', 'Assu'), ('Baia Formosa', 'Baía Formosa'), ('Baraúna', 'Baraúna'), ('Barcelona', 'Barcelona'), ('Bento Fernandes', 'Bento Fernandes'), ('Boa Saúde', 'Boa Saúde'), ('Bodó', 'Bodó'), ('Bom Jesus', 'Bom Jesus'), ('Brejinho', 'Brejinho'), ('Caicara do Norte', 'Caiçara do Norte'), ('Caicara do Rio do Vento', 'Caiçara do Rio do Vento'), ('Caicó', 'Caicó'), ('Campo Grande', 'Campo Grande'), ('Campo Redondo', 'Campo Redondo'), ('Canguaretama', 'Canguaretama'), ('Caraúbas', 'Caraúbas'), ('Carnauba dos Dantas', 'Carnaúba dos Dantas'), ('Carnaubais', 'Carnaubais'), ('Ceará Mirim', 'Ceará-Mirim'), ('Cerro corá', 'Cerro Corá'), ('Coronel Ezequiel', 'Coronel Ezequiel'), ('Coronel João Pessoa', 'Coronel João Pessoa'), ('cruzeta', 'Cruzeta'), ('Currais Novos', 'Currais Novos'), ('Doutor Severiano', 'Doutor Severiano'), ('Encanto', 'Encanto'), ('Equador', 'Equador'), ('Espirito Santo', 'Espírito Santo'), ('Extremoz', 'Extremoz'), ('Felipe Guerra', 'Felipe Guerra'), ('Fernando Pedroza', 'Fernando Pedroza'), ('Florãnia', 'Florânia'), ('Francisco Dantas', 'Francisco Dantas'), ('Frutuoso Gomes', 'Frutuoso Gomes'), ('Galinhos', 'Galinhos'), ('Goianinha', 'Goianinha'), ('Governador Dix-sept Rosado', 'Governador Dix-Sept Rosado'), ('Grossos', 'Grossos'), ('Guamaré', 'Guamaré'), ('Ielmo Marinho', 'Ielmo Marinho'), ('Ipanguaçu', 'Ipanguaçu'), ('Ipueira', 'Ipueira'), ('Itajá', 'Itajá'), ('Itaú', 'Itaú'), ('Jaçanã', 'Jaçanã'), ('Jandaíra', 'Jandaíra'), ('Janduís', 'Janduís'), ('Japi', 'Japi'), ('Jardim de Angicos', 'Jardim de Angicos'), ('Jardim de Piranhas', 'Jardim de Piranhas'), ('Jardim do seridó', 'Jardim do Seridó'), ('João Cãmara', 'João Câmara'), ('João Dias', 'João Dias'), ('José da Penha', 'José da Penha'), ('Jucurutu', 'Jucurutu'), ('Jundiá', 'Jundiá'), ('Lagoa d´Anta', 'Lagoa dAnta'), ('Lagoa de Pedras', 'Lagoa de Pedras'), ('Lagoa de Velhos', 'Lagoa de Velhos'), ('Lagoa Nova', 'Lagoa Nova'), ('Lagoa Salgada', 'Lagoa Salgada'), ('Lajes', 'Lajes'), ('Lajes Pintadas', 'Lajes Pintadas'), ('Lucrécia', 'Lucrécia'), ('Luis Gomes', 'Luís Gomes'), ('Macaiba', 'Macaíba'), ('Macau', 'Macau'), ('Major Sales', 'Major Sales'), ('Marcelino Vieira', 'Marcelino Vieira'), ('Martins', 'Martins'), ('Maxaranguape', 'Maxaranguape'), ('Messias Targino', 'Messias Targino'), ('Montanhas', 'Montanhas'), ('Monte Alegre', 'Monte Alegre'), ('Monte das Gameleiras', 'Monte das Gameleiras'), ('Mossoró', 'Mossoró'), ('Natal', 'Natal'), ('Nisia Floresta', 'Nísia Floresta'), ('Nova Cruz', 'Nova Cruz'), ('Olho d´Água doS Borges', 'Olho-dÁgua do Borges'), ('Parana', 'Paraná'), ('Parau', 'Paraú'), ('Parazinho', 'Parazinho'), ('Parelhas', 'Parelhas'), ('Parnamirim', 'Parnamirim'), ('Passa e Fica', 'Passa-e-Fica'), ('Passagem', 'Passagem'), ('Patu', 'Patu'), ('Pau dos Ferros', 'Pau dos Ferros'), ('Pedra Grande', 'Pedra Grande'), ('Pedra Preta', 'Pedra Preta'), ('Pedro Avelino', 'Pedro Avelino'), ('Pedro Velho', 'Pedro Velho'), ('Pendências', 'Pendências'), ('Pilões', 'Pilões'), ('Poço Branco', 'Poço Branco'), ('Portalegre', 'Portalegre'), ('Porto do Mangue', 'Porto do Mangue'), ('Pureza', 'Pureza'), ('Rafael Fernandes', 'Rafael Fernandes'), ('Rafael Godeiro', 'Rafael Godeiro'), ('Riacho da Cruz', 'Riacho da Cruz'), ('Riacho de Santana', 'Riacho de Santana'), ('Riachuelo', 'Riachuelo'), ('Rio do Fogo', 'Rio do Fogo'), ('Rodolfo Fernandes', 'Rodolfo Fernandes'), ('Santa Cruz', 'Santa Cruz'), ('Santa Maria', 'Santa Maria'), ('Santana do Matos', 'Santana do Matos'), ('Santana do Seridó', 'Santana do Seridó'), ('Santo Antônio', 'Santo Antônio'), ('São Bento do Norte', 'São Bento do Norte'), ('São Bento do Trairi', 'São Bento do Trairi'), ('São Fernando', 'São Fernando'), ('São Francisco do Oeste', 'São Francisco do Oeste'), ('São Gonçalo do Amarante', 'São Gonçalo do Amarante'), ('São João do Sabugi', 'São João do Sabugi'), ('São José de Mipibu', 'São José de Mipibu'), ('São José do Campestre', 'São José do Campestre'), ('São José do Seridó', 'São José do Seridó'), ('São Miguel', 'São Miguel'), ('São Miguel do Gostoso', 'São Miguel do Gostoso'), ('São Paulo do Potengi', 'São Paulo do Potengi'), ('São Pedro', 'São Pedro'), ('São Rafael', 'São Rafael'), ('São Tomé', 'São Tomé'), ('Senador Elói de Souza', 'Senador Elói de Souza'), ('senadorgeorginoavelino', 'Senador Georgino Avelino'), ('Serra Caiada', 'Serra Caiada'), ('Serra de São Bento', 'Serra de São Bento'), ('Serra do Mel', 'Serra do Mel'), ('Serra Negra do Norte', 'Serra Negra do Norte'), ('Serrinha', 'Serrinha'), ('Serrinha dos Pintos', 'Serrinha dos Pintos'), ('Severiano Melo', 'Severiano Melo'), ('Sitio Novo', 'Sítio Novo'), ('Taboleiro Grande', 'Taboleiro Grande'), ('Taipu', 'Taipu'), ('Tangará', 'Tangará'), ('Tenente Ananias', 'Tenente Ananias'), ('Tenentel Laurentino Cruz', 'Tenente Laurentino Cruz'), ('Tibau', 'Tibau'), ('Tibau do Sul', 'Tibau do Sul'), ('Timbaúba dos Batistas', 'Timbaúba dos Batistas'), ('Touros', 'Touros'), ('Triunfo Potiguar', 'Triunfo Potiguar'), ('Umarizal', 'Umarizal'), ('Upanema', 'Upanema'), ('Várzea', 'Várzea'), ('Venha-ver', 'Venha-Ver'), ('Vera Cruz', 'Vera Cruz'), ('Viçosa', 'Viçosa'), ('Vila Flor', 'Vila Flor')], max_length=30, verbose_name='Cidade:')),
                ('telefone_vaga', models.CharField(max_length=11, verbose_name='Telefone:')),
                ('Acrescenta', models.TextField(verbose_name='Descrição :')),
                ('email_vaga', models.EmailField(max_length=254, verbose_name='Email:')),
                ('criado_vaga', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('mudando_vaga', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome Completo :')),
                ('contato', models.CharField(max_length=13, verbose_name='Contato(WhatsApp), Formato 5584XXXXXXXXX')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email : *Opcional')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua :')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro :')),
                ('cidade', models.CharField(choices=[('Acari', 'Acari'), ('Afonso Bezerra', 'Afonso Bezerra'), ('Agua Nova', 'Água Nova'), ('Alexandria', 'Alexandria'), ('Almino Afonso', 'Almino'), ('Alto do Rodrigues', 'Alto do Rodrigues'), ('Angicos', 'Angicos'), ('Antônio Martins', 'Antônio Martins'), ('Apodi', 'Apodi'), ('Areia Branca', 'Areia Branca'), ('Arez', 'Arez'), ('Assu', 'Assu'), ('Baia Formosa', 'Baía Formosa'), ('Baraúna', 'Baraúna'), ('Barcelona', 'Barcelona'), ('Bento Fernandes', 'Bento Fernandes'), ('Boa Saúde', 'Boa Saúde'), ('Bodó', 'Bodó'), ('Bom Jesus', 'Bom Jesus'), ('Brejinho', 'Brejinho'), ('Caicara do Norte', 'Caiçara do Norte'), ('Caicara do Rio do Vento', 'Caiçara do Rio do Vento'), ('Caicó', 'Caicó'), ('Campo Grande', 'Campo Grande'), ('Campo Redondo', 'Campo Redondo'), ('Canguaretama', 'Canguaretama'), ('Caraúbas', 'Caraúbas'), ('Carnauba dos Dantas', 'Carnaúba dos Dantas'), ('Carnaubais', 'Carnaubais'), ('Ceará Mirim', 'Ceará-Mirim'), ('Cerro corá', 'Cerro Corá'), ('Coronel Ezequiel', 'Coronel Ezequiel'), ('Coronel João Pessoa', 'Coronel João Pessoa'), ('cruzeta', 'Cruzeta'), ('Currais Novos', 'Currais Novos'), ('Doutor Severiano', 'Doutor Severiano'), ('Encanto', 'Encanto'), ('Equador', 'Equador'), ('Espirito Santo', 'Espírito Santo'), ('Extremoz', 'Extremoz'), ('Felipe Guerra', 'Felipe Guerra'), ('Fernando Pedroza', 'Fernando Pedroza'), ('Florãnia', 'Florânia'), ('Francisco Dantas', 'Francisco Dantas'), ('Frutuoso Gomes', 'Frutuoso Gomes'), ('Galinhos', 'Galinhos'), ('Goianinha', 'Goianinha'), ('Governador Dix-sept Rosado', 'Governador Dix-Sept Rosado'), ('Grossos', 'Grossos'), ('Guamaré', 'Guamaré'), ('Ielmo Marinho', 'Ielmo Marinho'), ('Ipanguaçu', 'Ipanguaçu'), ('Ipueira', 'Ipueira'), ('Itajá', 'Itajá'), ('Itaú', 'Itaú'), ('Jaçanã', 'Jaçanã'), ('Jandaíra', 'Jandaíra'), ('Janduís', 'Janduís'), ('Japi', 'Japi'), ('Jardim de Angicos', 'Jardim de Angicos'), ('Jardim de Piranhas', 'Jardim de Piranhas'), ('Jardim do seridó', 'Jardim do Seridó'), ('João Cãmara', 'João Câmara'), ('João Dias', 'João Dias'), ('José da Penha', 'José da Penha'), ('Jucurutu', 'Jucurutu'), ('Jundiá', 'Jundiá'), ('Lagoa d´Anta', 'Lagoa dAnta'), ('Lagoa de Pedras', 'Lagoa de Pedras'), ('Lagoa de Velhos', 'Lagoa de Velhos'), ('Lagoa Nova', 'Lagoa Nova'), ('Lagoa Salgada', 'Lagoa Salgada'), ('Lajes', 'Lajes'), ('Lajes Pintadas', 'Lajes Pintadas'), ('Lucrécia', 'Lucrécia'), ('Luis Gomes', 'Luís Gomes'), ('Macaiba', 'Macaíba'), ('Macau', 'Macau'), ('Major Sales', 'Major Sales'), ('Marcelino Vieira', 'Marcelino Vieira'), ('Martins', 'Martins'), ('Maxaranguape', 'Maxaranguape'), ('Messias Targino', 'Messias Targino'), ('Montanhas', 'Montanhas'), ('Monte Alegre', 'Monte Alegre'), ('Monte das Gameleiras', 'Monte das Gameleiras'), ('Mossoró', 'Mossoró'), ('Natal', 'Natal'), ('Nisia Floresta', 'Nísia Floresta'), ('Nova Cruz', 'Nova Cruz'), ('Olho d´Água doS Borges', 'Olho-dÁgua do Borges'), ('Parana', 'Paraná'), ('Parau', 'Paraú'), ('Parazinho', 'Parazinho'), ('Parelhas', 'Parelhas'), ('Parnamirim', 'Parnamirim'), ('Passa e Fica', 'Passa-e-Fica'), ('Passagem', 'Passagem'), ('Patu', 'Patu'), ('Pau dos Ferros', 'Pau dos Ferros'), ('Pedra Grande', 'Pedra Grande'), ('Pedra Preta', 'Pedra Preta'), ('Pedro Avelino', 'Pedro Avelino'), ('Pedro Velho', 'Pedro Velho'), ('Pendências', 'Pendências'), ('Pilões', 'Pilões'), ('Poço Branco', 'Poço Branco'), ('Portalegre', 'Portalegre'), ('Porto do Mangue', 'Porto do Mangue'), ('Pureza', 'Pureza'), ('Rafael Fernandes', 'Rafael Fernandes'), ('Rafael Godeiro', 'Rafael Godeiro'), ('Riacho da Cruz', 'Riacho da Cruz'), ('Riacho de Santana', 'Riacho de Santana'), ('Riachuelo', 'Riachuelo'), ('Rio do Fogo', 'Rio do Fogo'), ('Rodolfo Fernandes', 'Rodolfo Fernandes'), ('Santa Cruz', 'Santa Cruz'), ('Santa Maria', 'Santa Maria'), ('Santana do Matos', 'Santana do Matos'), ('Santana do Seridó', 'Santana do Seridó'), ('Santo Antônio', 'Santo Antônio'), ('São Bento do Norte', 'São Bento do Norte'), ('São Bento do Trairi', 'São Bento do Trairi'), ('São Fernando', 'São Fernando'), ('São Francisco do Oeste', 'São Francisco do Oeste'), ('São Gonçalo do Amarante', 'São Gonçalo do Amarante'), ('São João do Sabugi', 'São João do Sabugi'), ('São José de Mipibu', 'São José de Mipibu'), ('São José do Campestre', 'São José do Campestre'), ('São José do Seridó', 'São José do Seridó'), ('São Miguel', 'São Miguel'), ('São Miguel do Gostoso', 'São Miguel do Gostoso'), ('São Paulo do Potengi', 'São Paulo do Potengi'), ('São Pedro', 'São Pedro'), ('São Rafael', 'São Rafael'), ('São Tomé', 'São Tomé'), ('Senador Elói de Souza', 'Senador Elói de Souza'), ('senadorgeorginoavelino', 'Senador Georgino Avelino'), ('Serra Caiada', 'Serra Caiada'), ('Serra de São Bento', 'Serra de São Bento'), ('Serra do Mel', 'Serra do Mel'), ('Serra Negra do Norte', 'Serra Negra do Norte'), ('Serrinha', 'Serrinha'), ('Serrinha dos Pintos', 'Serrinha dos Pintos'), ('Severiano Melo', 'Severiano Melo'), ('Sitio Novo', 'Sítio Novo'), ('Taboleiro Grande', 'Taboleiro Grande'), ('Taipu', 'Taipu'), ('Tangará', 'Tangará'), ('Tenente Ananias', 'Tenente Ananias'), ('Tenentel Laurentino Cruz', 'Tenente Laurentino Cruz'), ('Tibau', 'Tibau'), ('Tibau do Sul', 'Tibau do Sul'), ('Timbaúba dos Batistas', 'Timbaúba dos Batistas'), ('Touros', 'Touros'), ('Triunfo Potiguar', 'Triunfo Potiguar'), ('Umarizal', 'Umarizal'), ('Upanema', 'Upanema'), ('Várzea', 'Várzea'), ('Venha-ver', 'Venha-Ver'), ('Vera Cruz', 'Vera Cruz'), ('Viçosa', 'Viçosa'), ('Vila Flor', 'Vila Flor')], max_length=30, verbose_name='Cidade :')),
                ('estado', models.CharField(choices=[('RN', 'RN')], max_length=2, verbose_name='Estado :')),
                ('numero', models.CharField(max_length=100, verbose_name='Numero :')),
                ('profissao', models.CharField(max_length=100, verbose_name='Profissão :')),
                ('image', models.ImageField(upload_to='media/free', verbose_name='Imagem :')),
                ('Descricao', models.TextField(verbose_name='Descrição :')),
                ('termo', models.CharField(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=4, verbose_name='Você leu o Termo de Uso e a Política de privacidade ?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criando em:')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100, verbose_name='Nome do vendedor:')),
                ('Cidade_Vendedor', models.CharField(choices=[('Acari', 'Acari'), ('Afonso Bezerra', 'Afonso Bezerra'), ('Agua Nova', 'Água Nova'), ('Alexandria', 'Alexandria'), ('Almino Afonso', 'Almino'), ('Alto do Rodrigues', 'Alto do Rodrigues'), ('Angicos', 'Angicos'), ('Antônio Martins', 'Antônio Martins'), ('Apodi', 'Apodi'), ('Areia Branca', 'Areia Branca'), ('Arez', 'Arez'), ('Assu', 'Assu'), ('Baia Formosa', 'Baía Formosa'), ('Baraúna', 'Baraúna'), ('Barcelona', 'Barcelona'), ('Bento Fernandes', 'Bento Fernandes'), ('Boa Saúde', 'Boa Saúde'), ('Bodó', 'Bodó'), ('Bom Jesus', 'Bom Jesus'), ('Brejinho', 'Brejinho'), ('Caicara do Norte', 'Caiçara do Norte'), ('Caicara do Rio do Vento', 'Caiçara do Rio do Vento'), ('Caicó', 'Caicó'), ('Campo Grande', 'Campo Grande'), ('Campo Redondo', 'Campo Redondo'), ('Canguaretama', 'Canguaretama'), ('Caraúbas', 'Caraúbas'), ('Carnauba dos Dantas', 'Carnaúba dos Dantas'), ('Carnaubais', 'Carnaubais'), ('Ceará Mirim', 'Ceará-Mirim'), ('Cerro corá', 'Cerro Corá'), ('Coronel Ezequiel', 'Coronel Ezequiel'), ('Coronel João Pessoa', 'Coronel João Pessoa'), ('cruzeta', 'Cruzeta'), ('Currais Novos', 'Currais Novos'), ('Doutor Severiano', 'Doutor Severiano'), ('Encanto', 'Encanto'), ('Equador', 'Equador'), ('Espirito Santo', 'Espírito Santo'), ('Extremoz', 'Extremoz'), ('Felipe Guerra', 'Felipe Guerra'), ('Fernando Pedroza', 'Fernando Pedroza'), ('Florãnia', 'Florânia'), ('Francisco Dantas', 'Francisco Dantas'), ('Frutuoso Gomes', 'Frutuoso Gomes'), ('Galinhos', 'Galinhos'), ('Goianinha', 'Goianinha'), ('Governador Dix-sept Rosado', 'Governador Dix-Sept Rosado'), ('Grossos', 'Grossos'), ('Guamaré', 'Guamaré'), ('Ielmo Marinho', 'Ielmo Marinho'), ('Ipanguaçu', 'Ipanguaçu'), ('Ipueira', 'Ipueira'), ('Itajá', 'Itajá'), ('Itaú', 'Itaú'), ('Jaçanã', 'Jaçanã'), ('Jandaíra', 'Jandaíra'), ('Janduís', 'Janduís'), ('Japi', 'Japi'), ('Jardim de Angicos', 'Jardim de Angicos'), ('Jardim de Piranhas', 'Jardim de Piranhas'), ('Jardim do seridó', 'Jardim do Seridó'), ('João Cãmara', 'João Câmara'), ('João Dias', 'João Dias'), ('José da Penha', 'José da Penha'), ('Jucurutu', 'Jucurutu'), ('Jundiá', 'Jundiá'), ('Lagoa d´Anta', 'Lagoa dAnta'), ('Lagoa de Pedras', 'Lagoa de Pedras'), ('Lagoa de Velhos', 'Lagoa de Velhos'), ('Lagoa Nova', 'Lagoa Nova'), ('Lagoa Salgada', 'Lagoa Salgada'), ('Lajes', 'Lajes'), ('Lajes Pintadas', 'Lajes Pintadas'), ('Lucrécia', 'Lucrécia'), ('Luis Gomes', 'Luís Gomes'), ('Macaiba', 'Macaíba'), ('Macau', 'Macau'), ('Major Sales', 'Major Sales'), ('Marcelino Vieira', 'Marcelino Vieira'), ('Martins', 'Martins'), ('Maxaranguape', 'Maxaranguape'), ('Messias Targino', 'Messias Targino'), ('Montanhas', 'Montanhas'), ('Monte Alegre', 'Monte Alegre'), ('Monte das Gameleiras', 'Monte das Gameleiras'), ('Mossoró', 'Mossoró'), ('Natal', 'Natal'), ('Nisia Floresta', 'Nísia Floresta'), ('Nova Cruz', 'Nova Cruz'), ('Olho d´Água doS Borges', 'Olho-dÁgua do Borges'), ('Parana', 'Paraná'), ('Parau', 'Paraú'), ('Parazinho', 'Parazinho'), ('Parelhas', 'Parelhas'), ('Parnamirim', 'Parnamirim'), ('Passa e Fica', 'Passa-e-Fica'), ('Passagem', 'Passagem'), ('Patu', 'Patu'), ('Pau dos Ferros', 'Pau dos Ferros'), ('Pedra Grande', 'Pedra Grande'), ('Pedra Preta', 'Pedra Preta'), ('Pedro Avelino', 'Pedro Avelino'), ('Pedro Velho', 'Pedro Velho'), ('Pendências', 'Pendências'), ('Pilões', 'Pilões'), ('Poço Branco', 'Poço Branco'), ('Portalegre', 'Portalegre'), ('Porto do Mangue', 'Porto do Mangue'), ('Pureza', 'Pureza'), ('Rafael Fernandes', 'Rafael Fernandes'), ('Rafael Godeiro', 'Rafael Godeiro'), ('Riacho da Cruz', 'Riacho da Cruz'), ('Riacho de Santana', 'Riacho de Santana'), ('Riachuelo', 'Riachuelo'), ('Rio do Fogo', 'Rio do Fogo'), ('Rodolfo Fernandes', 'Rodolfo Fernandes'), ('Santa Cruz', 'Santa Cruz'), ('Santa Maria', 'Santa Maria'), ('Santana do Matos', 'Santana do Matos'), ('Santana do Seridó', 'Santana do Seridó'), ('Santo Antônio', 'Santo Antônio'), ('São Bento do Norte', 'São Bento do Norte'), ('São Bento do Trairi', 'São Bento do Trairi'), ('São Fernando', 'São Fernando'), ('São Francisco do Oeste', 'São Francisco do Oeste'), ('São Gonçalo do Amarante', 'São Gonçalo do Amarante'), ('São João do Sabugi', 'São João do Sabugi'), ('São José de Mipibu', 'São José de Mipibu'), ('São José do Campestre', 'São José do Campestre'), ('São José do Seridó', 'São José do Seridó'), ('São Miguel', 'São Miguel'), ('São Miguel do Gostoso', 'São Miguel do Gostoso'), ('São Paulo do Potengi', 'São Paulo do Potengi'), ('São Pedro', 'São Pedro'), ('São Rafael', 'São Rafael'), ('São Tomé', 'São Tomé'), ('Senador Elói de Souza', 'Senador Elói de Souza'), ('senadorgeorginoavelino', 'Senador Georgino Avelino'), ('Serra Caiada', 'Serra Caiada'), ('Serra de São Bento', 'Serra de São Bento'), ('Serra do Mel', 'Serra do Mel'), ('Serra Negra do Norte', 'Serra Negra do Norte'), ('Serrinha', 'Serrinha'), ('Serrinha dos Pintos', 'Serrinha dos Pintos'), ('Severiano Melo', 'Severiano Melo'), ('Sitio Novo', 'Sítio Novo'), ('Taboleiro Grande', 'Taboleiro Grande'), ('Taipu', 'Taipu'), ('Tangará', 'Tangará'), ('Tenente Ananias', 'Tenente Ananias'), ('Tenentel Laurentino Cruz', 'Tenente Laurentino Cruz'), ('Tibau', 'Tibau'), ('Tibau do Sul', 'Tibau do Sul'), ('Timbaúba dos Batistas', 'Timbaúba dos Batistas'), ('Touros', 'Touros'), ('Triunfo Potiguar', 'Triunfo Potiguar'), ('Umarizal', 'Umarizal'), ('Upanema', 'Upanema'), ('Várzea', 'Várzea'), ('Venha-ver', 'Venha-Ver'), ('Vera Cruz', 'Vera Cruz'), ('Viçosa', 'Viçosa'), ('Vila Flor', 'Vila Flor')], max_length=50, verbose_name='Cidade do vendedor:')),
                ('uf', models.CharField(choices=[('RN', 'RN')], max_length=50, verbose_name='UF. do vendedor')),
                ('Telefone', models.CharField(max_length=12, verbose_name='Telefone:')),
                ('Email_vendedor', models.CharField(max_length=60, verbose_name='Email do vendedor')),
                ('Conta_Bancaria', models.CharField(max_length=12, verbose_name='Conta Bancaria')),
                ('cpf', models.CharField(max_length=12, verbose_name='CPF do vendedor')),
                ('Codigo', models.CharField(max_length=12, verbose_name='COD. do vendedor')),
                ('Data_Inscricao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em :')),
                ('Alteracao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome Completo:')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefone(WhatsApp), 5584XXXXXXXXX:')),
                ('email', models.EmailField(max_length=254, verbose_name='Email:')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua:')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro:')),
                ('cidade', models.CharField(choices=[('Acari', 'Acari'), ('Afonso Bezerra', 'Afonso Bezerra'), ('Agua Nova', 'Água Nova'), ('Alexandria', 'Alexandria'), ('Almino Afonso', 'Almino'), ('Alto do Rodrigues', 'Alto do Rodrigues'), ('Angicos', 'Angicos'), ('Antônio Martins', 'Antônio Martins'), ('Apodi', 'Apodi'), ('Areia Branca', 'Areia Branca'), ('Arez', 'Arez'), ('Assu', 'Assu'), ('Baia Formosa', 'Baía Formosa'), ('Baraúna', 'Baraúna'), ('Barcelona', 'Barcelona'), ('Bento Fernandes', 'Bento Fernandes'), ('Boa Saúde', 'Boa Saúde'), ('Bodó', 'Bodó'), ('Bom Jesus', 'Bom Jesus'), ('Brejinho', 'Brejinho'), ('Caicara do Norte', 'Caiçara do Norte'), ('Caicara do Rio do Vento', 'Caiçara do Rio do Vento'), ('Caicó', 'Caicó'), ('Campo Grande', 'Campo Grande'), ('Campo Redondo', 'Campo Redondo'), ('Canguaretama', 'Canguaretama'), ('Caraúbas', 'Caraúbas'), ('Carnauba dos Dantas', 'Carnaúba dos Dantas'), ('Carnaubais', 'Carnaubais'), ('Ceará Mirim', 'Ceará-Mirim'), ('Cerro corá', 'Cerro Corá'), ('Coronel Ezequiel', 'Coronel Ezequiel'), ('Coronel João Pessoa', 'Coronel João Pessoa'), ('cruzeta', 'Cruzeta'), ('Currais Novos', 'Currais Novos'), ('Doutor Severiano', 'Doutor Severiano'), ('Encanto', 'Encanto'), ('Equador', 'Equador'), ('Espirito Santo', 'Espírito Santo'), ('Extremoz', 'Extremoz'), ('Felipe Guerra', 'Felipe Guerra'), ('Fernando Pedroza', 'Fernando Pedroza'), ('Florãnia', 'Florânia'), ('Francisco Dantas', 'Francisco Dantas'), ('Frutuoso Gomes', 'Frutuoso Gomes'), ('Galinhos', 'Galinhos'), ('Goianinha', 'Goianinha'), ('Governador Dix-sept Rosado', 'Governador Dix-Sept Rosado'), ('Grossos', 'Grossos'), ('Guamaré', 'Guamaré'), ('Ielmo Marinho', 'Ielmo Marinho'), ('Ipanguaçu', 'Ipanguaçu'), ('Ipueira', 'Ipueira'), ('Itajá', 'Itajá'), ('Itaú', 'Itaú'), ('Jaçanã', 'Jaçanã'), ('Jandaíra', 'Jandaíra'), ('Janduís', 'Janduís'), ('Japi', 'Japi'), ('Jardim de Angicos', 'Jardim de Angicos'), ('Jardim de Piranhas', 'Jardim de Piranhas'), ('Jardim do seridó', 'Jardim do Seridó'), ('João Cãmara', 'João Câmara'), ('João Dias', 'João Dias'), ('José da Penha', 'José da Penha'), ('Jucurutu', 'Jucurutu'), ('Jundiá', 'Jundiá'), ('Lagoa d´Anta', 'Lagoa dAnta'), ('Lagoa de Pedras', 'Lagoa de Pedras'), ('Lagoa de Velhos', 'Lagoa de Velhos'), ('Lagoa Nova', 'Lagoa Nova'), ('Lagoa Salgada', 'Lagoa Salgada'), ('Lajes', 'Lajes'), ('Lajes Pintadas', 'Lajes Pintadas'), ('Lucrécia', 'Lucrécia'), ('Luis Gomes', 'Luís Gomes'), ('Macaiba', 'Macaíba'), ('Macau', 'Macau'), ('Major Sales', 'Major Sales'), ('Marcelino Vieira', 'Marcelino Vieira'), ('Martins', 'Martins'), ('Maxaranguape', 'Maxaranguape'), ('Messias Targino', 'Messias Targino'), ('Montanhas', 'Montanhas'), ('Monte Alegre', 'Monte Alegre'), ('Monte das Gameleiras', 'Monte das Gameleiras'), ('Mossoró', 'Mossoró'), ('Natal', 'Natal'), ('Nisia Floresta', 'Nísia Floresta'), ('Nova Cruz', 'Nova Cruz'), ('Olho d´Água doS Borges', 'Olho-dÁgua do Borges'), ('Parana', 'Paraná'), ('Parau', 'Paraú'), ('Parazinho', 'Parazinho'), ('Parelhas', 'Parelhas'), ('Parnamirim', 'Parnamirim'), ('Passa e Fica', 'Passa-e-Fica'), ('Passagem', 'Passagem'), ('Patu', 'Patu'), ('Pau dos Ferros', 'Pau dos Ferros'), ('Pedra Grande', 'Pedra Grande'), ('Pedra Preta', 'Pedra Preta'), ('Pedro Avelino', 'Pedro Avelino'), ('Pedro Velho', 'Pedro Velho'), ('Pendências', 'Pendências'), ('Pilões', 'Pilões'), ('Poço Branco', 'Poço Branco'), ('Portalegre', 'Portalegre'), ('Porto do Mangue', 'Porto do Mangue'), ('Pureza', 'Pureza'), ('Rafael Fernandes', 'Rafael Fernandes'), ('Rafael Godeiro', 'Rafael Godeiro'), ('Riacho da Cruz', 'Riacho da Cruz'), ('Riacho de Santana', 'Riacho de Santana'), ('Riachuelo', 'Riachuelo'), ('Rio do Fogo', 'Rio do Fogo'), ('Rodolfo Fernandes', 'Rodolfo Fernandes'), ('Santa Cruz', 'Santa Cruz'), ('Santa Maria', 'Santa Maria'), ('Santana do Matos', 'Santana do Matos'), ('Santana do Seridó', 'Santana do Seridó'), ('Santo Antônio', 'Santo Antônio'), ('São Bento do Norte', 'São Bento do Norte'), ('São Bento do Trairi', 'São Bento do Trairi'), ('São Fernando', 'São Fernando'), ('São Francisco do Oeste', 'São Francisco do Oeste'), ('São Gonçalo do Amarante', 'São Gonçalo do Amarante'), ('São João do Sabugi', 'São João do Sabugi'), ('São José de Mipibu', 'São José de Mipibu'), ('São José do Campestre', 'São José do Campestre'), ('São José do Seridó', 'São José do Seridó'), ('São Miguel', 'São Miguel'), ('São Miguel do Gostoso', 'São Miguel do Gostoso'), ('São Paulo do Potengi', 'São Paulo do Potengi'), ('São Pedro', 'São Pedro'), ('São Rafael', 'São Rafael'), ('São Tomé', 'São Tomé'), ('Senador Elói de Souza', 'Senador Elói de Souza'), ('senadorgeorginoavelino', 'Senador Georgino Avelino'), ('Serra Caiada', 'Serra Caiada'), ('Serra de São Bento', 'Serra de São Bento'), ('Serra do Mel', 'Serra do Mel'), ('Serra Negra do Norte', 'Serra Negra do Norte'), ('Serrinha', 'Serrinha'), ('Serrinha dos Pintos', 'Serrinha dos Pintos'), ('Severiano Melo', 'Severiano Melo'), ('Sitio Novo', 'Sítio Novo'), ('Taboleiro Grande', 'Taboleiro Grande'), ('Taipu', 'Taipu'), ('Tangará', 'Tangará'), ('Tenente Ananias', 'Tenente Ananias'), ('Tenentel Laurentino Cruz', 'Tenente Laurentino Cruz'), ('Tibau', 'Tibau'), ('Tibau do Sul', 'Tibau do Sul'), ('Timbaúba dos Batistas', 'Timbaúba dos Batistas'), ('Touros', 'Touros'), ('Triunfo Potiguar', 'Triunfo Potiguar'), ('Umarizal', 'Umarizal'), ('Upanema', 'Upanema'), ('Várzea', 'Várzea'), ('Venha-ver', 'Venha-Ver'), ('Vera Cruz', 'Vera Cruz'), ('Viçosa', 'Viçosa'), ('Vila Flor', 'Vila Flor')], max_length=30, verbose_name='Cidade:')),
                ('estado', models.CharField(choices=[('RN', 'RN')], max_length=2, verbose_name='Estado:')),
                ('numero', models.CharField(max_length=100, verbose_name='Número:')),
                ('profissao', models.CharField(max_length=100, verbose_name='Profissão:')),
                ('image', models.ImageField(upload_to='media/premium', verbose_name='Foto do Perfil:')),
                ('premium', models.CharField(choices=[('PREMIUM', 'PREMIUM')], max_length=7, verbose_name='Sou PREMIUM ?:')),
                ('Descricao', models.TextField(verbose_name='Descreva um pouco de suas habilidades ....')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Criado Por:')),
            ],
        ),
        migrations.CreateModel(
            name='Pdfs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profissao', models.CharField(max_length=100, verbose_name='SUA PROFISSÃO ?')),
                ('pdf', models.FileField(upload_to='media/pdf/', verbose_name='CURRÍCULO')),
                ('criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Enviado Por:')),
            ],
        ),
        migrations.CreateModel(
            name='Incricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_candidato', models.CharField(max_length=50, verbose_name='Nome Completo:')),
                ('telefone_candidato', models.CharField(max_length=12, verbose_name='Telefone de contato:')),
                ('inscricao_criada', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('inscricao_editada', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='paginas.processos', verbose_name='CONFIRME A EMPRESA')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='PROFISSIONAL PARTICIPANTE')),
            ],
        ),
    ]
