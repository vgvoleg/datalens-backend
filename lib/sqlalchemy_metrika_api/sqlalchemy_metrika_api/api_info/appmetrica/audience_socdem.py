audience_socdem_fields = [
    {
        'description': '',
        'is_dim': False,
        'name': 'ym:u:sessions',
        'title': 'Количество сессий',
        'type': 'integer'
    },
    {
        'description': '',
        'is_dim': False,
        'name': 'ym:u:newUsers',
        'title': 'Новые пользователи',
        'type': 'integer'
    },
    {
        'description': '',
        'is_dim': False,
        'name': 'ym:u:activeUsers',
        'title': 'Пользователи',
        'type': 'integer'
    },
    {
        'description': 'Пол посетителя. Возможные значения: "мужской" или "женский".',
        'is_dim': True,
        'name': 'ym:u:genderName',
        'title': 'Пол',
        'type': 'string',
    },
    {
        'description': 'Возраст посетителя, интервал',
        'is_dim': True,
        'name': 'ym:u:ageIntervalName',
        'title': 'Возраст',
        'type': 'string',
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:isRooted',
        'title': 'Root-статус',
        'type': 'string'
    },
    {
        'description': 'Идентификатор приложения',
        'is_dim': True,
        'name': 'ym:u:apiKey',
        'title': 'ID приложения',
        'type': 'string',
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:clientKitVersion',
        'title': 'Версия SDK клиента',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:operatingSystemVersionInfo',
        'title': 'Версия платформы',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:appVersion',
        'title': 'Версия приложения',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:year',
        'title': 'Год',
        'type': 'integer'
    },
    {
        'description': 'Название города, к которому принадлежат посетители сайта.',
        'is_dim': True,
        'name': 'ym:u:regionCityName',
        'title': 'Город',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:date',
        'title': 'Дата',
        'type': 'date'
    },
    {
        'description': 'Дата и время в формате YYYY-MM-DD HH:mm:ss, округленное до начала года.',
        'is_dim': True,
        'name': 'ym:u:startOfYear',
        'title': 'Дата (год)',
        'type': 'date'
    },
    {
        'description': 'Дата и время в формате YYYY-MM-DD HH:mm:ss, округленное до начала 10-минутного интервала.',
        'is_dim': True,
        'name': 'ym:u:startOfDekaminute',
        'title': 'Дата (декаминута)',
        'type': 'datetime'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:startOfQuarter',
        'title': 'Дата (квартал)',
        'type': 'date'
    },
    {
        'description': 'Дата и время в формате YYYY-MM-DD HH:mm:ss, округленное до начала месяца.',
        'is_dim': True,
        'name': 'ym:u:startOfMonth',
        'title': 'Дата (месяц)',
        'type': 'date'
    },
    {
        'description': 'Дата и время в формате YYYY-MM-DD HH:mm:ss, округленное до начала минуты.',
        'is_dim': True,
        'name': 'ym:u:startOfMinute',
        'title': 'Дата (минута)',
        'type': 'datetime'
    },
    {
        'description': 'Дата и время в формате YYYY-MM-DD HH:mm:ss, округленное до начала часа.',
        'is_dim': True,
        'name': 'ym:u:startOfHour',
        'title': 'Дата (час)',
        'type': 'datetime'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:dekaminute',
        'title': 'Декаминута',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:dayOfMonth',
        'title': 'День месяца',
        'type': 'integer'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:dayOfWeekName',
        'title': 'День недели',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:appID',
        'title': 'Идентификатор приложения (в магазине приложений)',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:osMajorVersionInfoName',
        'title': 'Мажорная версия ОС',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:clientKitVersionDetails',
        'title': 'Информация о версии SDK',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:month',
        'title': 'Месяц',
        'type': 'integer'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:minute',
        'title': 'Минута',
        'type': 'integer'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:mobileDeviceModel',
        'title': 'Модель',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:mpcName',
        'title': 'Название сотового оператора на основе кода сотового оператора (MPC)',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:mccName',
        'title': 'Название страны на основе мобильного кода страны оператора (MCC)',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:buildNumber',
        'title': 'Номер сборки приложения',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:regionAreaName',
        'title': 'Область',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:operatingSystemInfoName',
        'title': 'Операционная система',
        'type': 'string'
    },
    {
        'description': 'Возможные значения: "yes", "no", "undefined".',
        'is_dim': True,
        'name': 'ym:u:limitAdTracking',
        'title': 'Признак ограничения рекламного трекинга',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:mobileDeviceBranding',
        'title': 'Производитель',
        'type': 'string'
    },
    {
        'description': 'Подробная информация о разрешении экрана. Например, "2560x1440 px (xxxhdpi)".',
        'is_dim': True,
        'name': 'ym:u:screenResolutionDetailed',
        'title': 'Разрешение (подробно)',
        'type': 'string'
    },
    {
        'description': 'Название страны, к которой принадлежат посетители сайта.',
        'is_dim': True,
        'name': 'ym:u:regionCountryName',
        'title': 'Страна',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:connectionType',
        'title': 'Тип подключения: Cellular или Wi-Fi',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:networkType',
        'title': 'Тип сети: 3G, EDGE и т.д.',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:deviceTypeName',
        'title': 'Тип устройства',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:hour',
        'title': 'Час',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:hourMinute',
        'title': 'Час и минута',
        'type': 'string'
    },
    {
        'description': None,
        'is_dim': True,
        'name': 'ym:u:locale',
        'title': 'Язык интерфейса',
        'type': 'string'
    },
]
