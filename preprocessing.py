import pandas as pd

def preprocessing_csv(from_file_path: str, to_file_path: str) -> None:
    """
    csv파일 중에서 필요한 col만 남겨두는 함수입니다.

    Args:
        from_file_path (str): 읽어올 csv파일의 위치를 지정합니다.
        to_file_path (str): 저장할 csv파일의 이름입니다.

    Raises:
        ValueError: 필요한 인자가 누락되었을 때 오류를 발생시킵니다.
    """
    # 입력값 검증
    if not from_file_path or not to_file_path:
        raise ValueError("from_file_path or to_file_path is required but not provided.")
    
    table_df = pd.read_csv(from_file_path)
    
    remain_cols = ['학과(부)', '학년', '이수구분', '학수번호', '교과목명', '담당교수', '시간표(교시)', '시간표(시간)', '학점', '수업유형']
    
    drop_cols = set(table_df.columns) - set(remain_cols)
    
    table_df.drop(drop_cols, axis=1, inplace=True)
    table_df.to_csv(to_file_path)
    
    return


def find_max_length_df(df_col:pd.DataFrame) -> int:
    """
    특정 col에서 가장 긴 길이가 몇인지를 반환하는 함수입니다.

    Args:
        df_col (pd.DataFrame): DataFrame에서 특정 col을 입력으로합니다.

    Returns:
        int: col_max_length
    """
    
    max_length_df = df_col.map(len).max()
    
    return max_length_df


if __name__ == "__main__":
    df = pd.read_csv('2024-1-')