from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite 데이터베이스 파일 생성
DATABASE_URL = "sqlite:///example.db"

# 데이터베이스 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)

# 기본 클래스 생성
Base = declarative_base()

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users"  # 테이블 이름

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, age={self.age}, email={self.email})>"


# 테이블 생성
Base.metadata.create_all(engine)
print("데이터베이스와 테이블 생성 완료")



# 함수 정의
def insert_user(name, age, email):
    """사용자 추가 (중복 이메일은 무시)"""
    user = User(name=name, age=age, email=email)
    try:
        session.add(user)
        session.commit()
        print(f"Inserted: {user}")
    except Exception as e:
        session.rollback()  # 충돌 시 롤백
        print(f"Failed to insert {email}: {e}")

def delete_user(email):
    """사용자 삭제"""
    user = session.query(User).filter(User.email == email).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"Deleted: {user}")
    else:
        print(f"No user found with email: {email}")

def query_users():
    """사용자 조회"""
    users = session.query(User).all()
    print("\nUsers in Database:")
    for user in users:
        print(user)



# 2. 데이터 입력 (멱등성 보장)
insert_user(name="John Doe", age=30, email="john.doe@example.com")
insert_user(name="Jane Smith", age=25, email="jane.smith@example.com")
insert_user(name="Alice Johnson", age=28, email="alice.johnson@example.com")

# 3. 중복 데이터 입력 시도 (멱등성 확인)
insert_user(name="John Doe", age=30, email="john.doe@example.com")

# 4. 데이터 조회
query_users()

# 5. 데이터 삭제
delete_user(email="alice.johnson@example.com")

# 6. 데이터 조회 (삭제 확인)
query_users()

