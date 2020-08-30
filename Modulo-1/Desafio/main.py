from datetime import datetime, timedelta

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def calculate_call_price(start, end):
    callStart = datetime.fromtimestamp(start)
    callEnd = datetime.fromtimestamp(end)
    tax = 0.36
    # percorre a duração da chamada enquanto os segundos fecham o
    # ciclo de 60 segundos(1 minuto)
    while callStart < callEnd and (callEnd - callStart).total_seconds() >= 60:
        # verifica se o minuto se encontra dentro do período tarifado
        if callStart.hour >= 6 and callStart.hour < 22:
            tax = tax + 0.09
        # incrementa 1 minuto no início da chamada
        callStart = callStart + timedelta(minutes=1)
    return tax

def filter_records(records):

    results = []
    # percorre cada registro da lista inicial
    for record in records:
        i = 0
        # retorna o valor da chamada do registro da vez no loop
        price = calculate_call_price(record['start'], record['end'])
        # percorre cada registro da lista que está sendo gerada 
        for result in results:
            # verifica se o registro da vez já foi adicionado
            # à nova lista
            if result['source'] == record['source']:
                i = 1
                # caso já esteja na nova lista apenas somamos
                # os valores
                result['total'] = result['total'] + price
        if i == 0:
            # adiciona o registro a nova lista quando inexistente
            results.append({'source': record['source'], 'total': price})
    return results

def classify_by_phone_number(records):

    results = []
    # filtra as ligações unindo ligações do mesmo número
    # calculando o valor total
    calls = filter_records(records)
    # após o cálculo terminado percore cada resgistro
    # formatando o valor total com 2 casas após a vírgula
    for call in calls:
        results.append({'source': call['source'], 'total': round(call['total'], 2)})
    # ordena a lista por valor em ordem decrescente
    results = sorted(results, key=lambda x: x['total'], reverse=True)

    return results
