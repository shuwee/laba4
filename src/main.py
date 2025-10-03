from Models.cargo import TransportCalculator


def main():
    print("=== Калькулятор стоимости перегрузки грузов v1.0 ===")
    calculator = TransportCalculator()

    try:
        weight = float(input("Введите вес груза (кг): "))
        if weight <= 0:
            print("Ошибка: вес должен быть положительным числом")
            return

        floor = int(input("Введите целевой этаж: "))
        if floor < 1:
            print("Ошибка: этаж должен быть положительным числом")
            return

        has_elevator = input("Есть ли лифт? (y/n): ").lower() == 'y'

        result = calculator.calculate_total_cost(weight, floor, has_elevator)

        print(f"\n=== РАСЧЕТ СТОИМОСТИ ===")
        print(f"Вес груза: {weight} кг")
        print(f"Целевой этаж: {floor}")
        print(f"Наличие лифта: {'да' if has_elevator else 'нет'}")
        print(f"Базовая стоимость: {result['base_cost']} руб.")

        if not has_elevator:
            print(f"Количество этажей подъема: {result['floors_to_climb']}")
            print(f"Единицы веса (по 100 кг): {result['weight_units']}")
            print(f"Стоимость ручного подъема: {result['manual_cost']} руб.")

        print(f"ОБЩАЯ СТОИМОСТЬ: {result['total_cost']} руб.")

        if not has_elevator and result['manual_cost'] > 0:
            print(f"\nДетализация ручного подъема:")
            print(
                f"300 руб/этаж × {result['floors_to_climb']} этаж(а/ей) × {result['weight_units']} ед.веса = {result['manual_cost']} руб.")

    except ValueError:
        print("Ошибка: введите корректные числовые значения")



if __name__ == "__main__":
    main()
