from app.knights.models import Knight
from app.knights.config import KNIGHTS


def battle(knights_config: dict) -> dict:
    # 1. Створюємо об'єкти лицарів (це автоматично рахує їх стати)
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # 2. Проводимо бої

    # Lancelot vs Mordred
    # Формула: damage = opponent_power - self_protection
    lancelot.take_damage(mordred.power - lancelot.protection)
    mordred.take_damage(lancelot.power - mordred.protection)

    # Arthur vs Red Knight
    arthur.take_damage(red_knight.power - arthur.protection)
    red_knight.take_damage(arthur.power - red_knight.protection)

    # 3. Повертаємо результат
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


# Цей рядок потрібен, щоб можна було запустити файл і перевірити результат
if __name__ == "__main__":
    print(battle(KNIGHTS))
