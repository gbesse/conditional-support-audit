# conditional-support-audit

## Français

Repérer les combinaisons synthétiques absentes de la référence.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m conditional_support_audit examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Compare le support empirique conjoint par sous-ensembles de colonnes et garde NULL/types distincts ; montre les créations de combinaisons qu’un contrôle marginal manquerait.

### Limites

Absence dans un échantillon ne signifie pas impossibilité métier ; ni causalité ni test de confidentialité.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Find synthetic combinations absent from reference support.

Synthetic data; no network access or secret required.

```sh
python -m conditional_support_audit examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Compares empirical joint support over column subsets and preserves NULL/type distinctions; exposes created combinations that marginal checks miss.

### Limits

Absence from a sample does not mean business impossibility; no causality or privacy test.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Encontrar combinaciones sintéticas ausentes del soporte de referencia.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m conditional_support_audit examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Compara soporte conjunto empírico por subconjuntos de columnas y conserva NULL/tipos; expone combinaciones nuevas omitidas por controles marginales.

### Límites

Ausencia en muestra no significa imposibilidad de negocio; sin causalidad ni prueba de privacidad.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.sdv.dev/sdmetrics/data-metrics/quality
